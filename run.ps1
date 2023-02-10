# Activate venv?

# D:\usr\dmacdonald\source\repos\library\api\app.py
# gunicorn --access-logfile - --error-logfile - --log-level error --config myapp/config.py myapp.app:app
# $env:FLASK_APP='D:\usr\dmacdonald\source\repos\library\api\app.py:app'; flask run

$PyPaths = 'D:\usr\dmacdonald\source\repos\library\api;D:\usr\dmacdonald\source\repos\library\venv\Lib\site-packages\'
if ($env:PYTHONPATH) {
    $env:PYTHONPATH = $PyPaths
} else {
    $env:PYTHONPATH += ';' + $PyPaths
}
python3 D:\usr\dmacdonald\source\repos\library\api\app.py