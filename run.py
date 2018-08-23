#-*- encoding: utf-8 -*-
import os
from app import appcontext as ctx

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5050))
	ctx.app.run(host="0.0.0.0", port = port, debug=True)
