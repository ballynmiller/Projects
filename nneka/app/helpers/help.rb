module Sinatra
	module Help
		def partial(path, locals = {})
		  parts = path.split('/')
		  parts[-1] = '_' + parts[-1]
		  slim parts.join('/').to_sym, locals: locals
		end

		def get_album_titles
			return Dir.entries(File.dirname(__FILE__) + '/../static/images') \
				.delete_if {|dir| dir.include? '.'}
		end

		def get_first_img(album_name)
			photos = Dir.entries(File.dirname(__FILE__) + "/../static/images/" + album_name) \
				.delete_if {|f| File.directory? f or f.include? "DS_Store"}
			unless photos.empty?
				return album_name + "/" + photos[0]
			end
		end
	end
	helpers Help
end
