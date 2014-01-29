# main rb for the site
require 'sinatra'
require 'sinatra/reloader' if development?
require 'slim'

require_relative 'helpers/help'

# update public folder 
set :public_folder, File.dirname(__FILE__) + '/static'

#config slim
Slim::Engine.default_options[:pretty] = true


get '/' do
	slim :index
end

get '/about' do
end 

get '/portfolio/:album_name' do |a|
	if Dir.exists?("static/images/#{a}")
		photos = []
		for photo in Dir.glob("static/images/#{a}/*.*") do
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