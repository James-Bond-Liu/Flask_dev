from flask import Flask
app = Flask(__name__)

# app.config其实是实例化了flask.config.Config类的实例，字典dict结构
app.config['DEBUG'] = True
# app.config.update(DEBUG=True)


@app.route('/')
def run():
    return 'welcom to my world'

if __name__ == '__main__':
    app.run()

"""

配置项名称	说明
DEBUG	启用/禁用调试模式

TESTING	启用/禁用测试模式

PROPAGATE_EXCEPTIONS	显式地允许或禁用异常的传播。如果没有设置或显式地设置为 None ，当 TESTING 或 DEBUG 为真时，这个值隐式地为 true.

PRESERVE_CONTEXT_ON_EXCEPTION	默认情况下，如果应用工作在调试模式，请求上下文不会在异常时出栈来允许调试器内省。 这可以通过这个键来禁用。你同样可以用这个设定来强制启用它，即使没有调试执行，这对调试生产应用很有用（但风险也很大）

SECRET_KEY	密钥

SESSION_COOKIE_NAME	会话 cookie 的名称。

SESSION_COOKIE_DOMAIN	会话 cookie 的域。如果不设置这个值，则 cookie 对 SERVER_NAME 的全部子域名有效

SESSION_COOKIE_PATH	会话 cookie 的路径。如果不设置这个值，且没有给 '/' 设置过，则 cookie 对 APPLICATION_ROOT 下的所有路径有效。

SESSION_COOKIE_HTTPONLY	控制 cookie 是否应被设置 httponly 的标志， 默认为 True

SESSION_COOKIE_SECURE	控制 cookie 是否应被设置安全标志，默认为 False

PERMANENT_SESSION_LIFETIME	以datetime.timedelta对象控制长期会话的生存时间。从 Flask 0.8 开始，也可以用整数来表示秒。

SESSION_REFRESH_EACH_REQUEST	这个标志控制永久会话如何刷新。如果被设置为 True （这是默认值），每一个请求 cookie 都会被刷新。如果设置为 False ，只有当 cookie 被修改后才会发送一个 set-cookie 的标头。非永久会话不会受到这个配置项的影响 。

USE_X_SENDFILE	启用/禁用 x-sendfile

LOGGER_NAME	日志记录器的名称

SERVER_NAME	服务器名和端口。需要这个选项来支持子域名 （例如： 'myapp.dev:5000' ）。注意 localhost 不支持子域名，所以把这个选项设置为 “localhost” 没有意义。设置 SERVER_NAME 默认会允许在没有请求上下文而仅有应用上下文时生成 URL

APPLICATION_ROOT	如果应用不占用完整的域名或子域名，这个选项可以被设置为应用所在的路径。这个路径也会用于会话 cookie 的路径值。如果直接使用域名，则留作 None

MAX_CONTENT_LENGTH	如果设置为字节数， Flask 会拒绝内容长度大于此值的请求进入，并返回一个 413 状态码

SEND_FILE_MAX_AGE_DEFAULT	默认缓存控制的最大期限，以秒计，在flask.Flask.send_static_file()(默认的静态文件处理器)中使用。对于单个文件分别在 Flask或Blueprint上使用get_send_file_max_age()来覆盖这个值。默认为 43200（12小时）。

TRAP_HTTP_EXCEPTIONS	如果这个值被设置为 True ，Flask不会执行 HTTP 异常的错误处理，而是像对待其它异常一样， 通过异常栈让它冒泡地抛出。这对于需要找出 HTTP 异常源头的可怕调试情形是有用的。

TRAP_BAD_REQUEST_ERRORS	Werkzeug 处理请求中的特定数据的内部数据结构会抛出同样也是“错误的请求”异常的特殊的 key errors 。同样地，为了保持一致，许多操作可以显式地抛出 BadRequest 异常。因为在调试中，你希望准确地找出异常的原因，这个设置用于在这些情形下调试。如果这个值被设置为 True ，你只会得到常规的回溯。

PREFERRED_URL_SCHEME	生成URL的时候如果没有可用的 URL 模式话将使用这个值。默认为 http

JSON_AS_ASCII	默认情况下 Flask 使用 ascii 编码来序列化对象。如果这个值被设置为 False ， Flask不会将其编码为 ASCII，并且按原样输出，返回它的 unicode 字符串。比如 jsonfiy 会自动地采用 utf-8 来编码它然后才进行传输。

JSON_SORT_KEYS	默认情况下 Flask 按照 JSON 对象的键的顺序来序来序列化它。这样做是为了确保键的顺序不会受到字典的哈希种子的影响，从而返回的值每次都是一致的，不会造成无用的额外 HTTP 缓存。你可以通过修改这个配置的值来覆盖默认的操作。但这是不被推荐的做法因为这个默认的行为可能会给你在性能的代价上带来改善。

JSONIFY_PRETTYPRINT_REGULAR	如果这个配置项被 True （默认值）， 如果不是 XMLHttpRequest 请求的话（由 X-Requested-With 标头控制） json 字符串的返回值会被漂亮地打印出来。

"""