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
	end
	helpers Help
end
