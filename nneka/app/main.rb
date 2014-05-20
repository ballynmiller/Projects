# main rb for the site
require 'sinatra/base'
require 'slim'

require_relative 'helpers/help'

class Portfolio < Sinatra::Base

	include Sinatra::Help

	# update public folder 
	set :public_folder, File.dirname(__FILE__) + '/static'

	# config slim
	Slim::Engine.default_options[:pretty] = true

	get '/' do
		slim :index
	end

	get '/about' do
		slim :about
	end 

	get '/portfolio/:album_name' do |a|
		dirname = File.dirname(__FILE__) + "/static/images/#{a}"
		if Dir.exists?(dirname)
			photos = []
			for photo in Dir.glob(dirname + "/*.*") do
				photos.push(photo[/\/images\/.*/])
			end
			slim :_photos, :locals => {:photos => photos}
		else
			halt 404
		end
	end

	get '/rates' do
	end

	get '/contact' do
	end

	error 404 do
		'Not Found'
	end
end
