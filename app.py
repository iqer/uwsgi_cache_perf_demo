import sys
import pickle

from flask import Flask


app = Flask(__name__)

try:
    import uwsgi
    print('uwsgi is imported.')
except:
    print('Not running from uwsgi')

num = 0


@app.route('/set')
def demo_set():
    # demo = TestDemo()
    # print(str(demo))
    # print(sys.getsizeof(demo))
    demo = 'a' * 2000
    print('++++++++++++++++++++++++++')
    print('Size:', sys.getsizeof(demo))
    print('++++++++++++++++++++++++++')

    try:
        # for k, v in uwsgi.__dict__.iteritems():
        #     print('{}: {}'.format(k, v))
        # from remote_pdb import RemotePdb

        # RemotePdb('127.0.0.1', 4444).set_trace()
        # demo = uwsgi.cache_exists('demo')
        global num
        if num > 10:
            num = 0
        key = 'cache_{}'.format(num)
        demo = pickle.dumps(demo)
        uwsgi.cache_set(key, demo, 0, 'mycache')
        print(len(uwsgi.cache_get(key, 'mycache')))
        num += 1
        return str(num)

    except:
        import traceback
        print(traceback.print_exc())
        return 'not set'


@app.route('/get')
def demo_get():
    demo = ''
    try:
        # for k, v in uwsgi.__dict__.iteritems():
        #     print('{}: {}'.format(k, v))
        # from remote_pdb import RemotePdb

        # RemotePdb('127.0.0.1', 4444).set_trace()
        # demo = uwsgi.cache_exists('demo')
        global num

        key = 'cache_{}'.format(num - 1)
        demo = uwsgi.cache_get(key, 'mycache')
        print('demo:', demo)
        demo = pickle.loads(demo)

    except:
        import traceback
        print(traceback.print_exc())
    return demo or 'not get'


if __name__ == '__main__':
    app.run(debug=True)
