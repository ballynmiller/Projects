# config valid only for current version of Capistrano
lock '3.3.5'

set :application, 'websites'
set :repo_url, 'git@github.com:ballynmiller/Sites.git'
set :branch, :master
set :deploy_to, "/var/www/#{fetch(:application)}"
set :nginx_path, "/etc/nginx/sites-enabled/"

namespace :deploy do
	task :create_configs do
		on roles(:all) do
			execute "ln -s #{current_path}/django_apps/etc #{shared_path}/etc"
			execute "cp #{shared_path}/etc/jakore #{fetch(:nginx_path)}/jakore"
		end
	end

	task :create_virtual_env do
		on roles(:all) do
			execute "virtualenv #{current_path}/django_apps/websites/.venv"
		end
	end
end

before :deploy, :kill_nginx do
	on roles(:all) do
		if test("[ -f /tmp/run/jakore.pid ]")
			execute "kill -HUP $(cat /tmp/run/jakore.pid)"
		end
	end
end

before :deploy, :cleanup_files do
	on roles(:all) do
		if test("[ -d #{shared_path} ]")
			execute "rm -rf #{shared_path}"
		end

		if test("[ -d /tmp/run ]")
			execute "rm -rf /tmp/run"
		end
	end
end

after :deploy, :start_nginx do
	on roles(:all) do
		invoke "deploy:create_configs"
		invoke "deploy:create_virtual_env"
		execute ". #{current_path}/django_apps/websites/.venv/bin/activate"
		execute "pip install -Ur #{current_path}/django_apps/requirements.txt"
		invoke "maintenance:start"
	end
end

namespace :maintenance do
	desc "Starts nginx server for application"
	task :start do
		on roles(:web) do
			if !Dir.exists?("/tmp/run")
				execute "mkdir /tmp/run"
			end
			
			# update settings file
			execute "sed -i 's/{PASSWORD}/84||yn23/g' #{current_path}/django_apps/websites/jakore_settings.py"
			execute "sed -i 's/{EMAIL_HOST}/ballyn.miller@gmail.com/g' #{current_path}/django_apps/websites/jakore_settings.py"
			execute "sed -i 's/{EMAIL_PASSWORD}/ccsphhmagmdvqlxo/g' #{current_path}/django_apps/websites/jakore_settings.py"

			#update jakore file
			execute "sed -i 's/{ASSETS_PATH}/\\/var\\/www\\/websites\\/current\\/django_apps\\/media/g' /etc/nginx/sites-enabled/jakore"

			# update uwsgi file
			execute "sed -i 's/{PATH}/\\/var\\/www\\/websites\\/current\\/django_apps/g' #{shared_path}/etc/uwsgi.ini"
			execute "uwsgi --ini #{shared_path}/etc/uwsgi.ini"

			# reload nginx
			execute "service nginx reload"
		end
	end

	desc "Kills nginx server for application"
	task :stop do
		on roles(:web) do
			if test("[ -f /var/run/jakore.pid ]")
				execute "kill -HUP $(cat /var/run/jakore.pid)"
			end
		end
	end

	desc "Restarts nginx for application"
	task :restart do
		on roles(:web) do
			invoke "maintenance:stop"
			invoke "maintenance:start"
		end
	end
end
