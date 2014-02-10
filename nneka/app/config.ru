require 'sinatra'
require './main.rb'

configure :development do
	require 'sinatra/reloader'
end

run Portfolio