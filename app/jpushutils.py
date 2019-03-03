
from app import config
import jpush
_jpush = jpush.JPush(config.app_key, config.master_secret)
_jpush.set_logging("DEBUG")



def all():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response=push.send()
        return response
    except jpush.common.Unauthorized:
        raise jpush.common.Unauthorized("Unauthorized")
    except jpush.common.APIConnectionException:
        raise jpush.common.APIConnectionException("conn")
    except jpush.common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")


def alias(alias,action):
    message = {"action":action}
    push = _jpush.create_push()
    alias=[alias]
    alias1={"alias": alias}
    push.audience = jpush.audience(
        alias1
    )
    push.message=jpush.message(message)
    push.platform = jpush.all_
    return push.send()