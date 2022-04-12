import re
import string
import hoshino
from hoshino import aiorequests
from hoshino import Service,priv

sv = Service(
    name = '撤回bot信息')
    
@sv.on_rex("撤回bot信息")#可以根据需求更改触发指令，对话中包含该关键词都会触发bot，但只有回复才会触发，如果需要撤回2分钟之前的可以授予管理员权限
async def wear(bot, ev):
    cq = str(ev.message)#获取CQ码
    num = 13
    st = int(cq.find('[CQ:reply,id='))
    if st == -1:
        msg_text = f"你发的不是回复"#可以根据需求注释或修改回复
        await bot.send(ev, msg_text)
    else:
        while cq[num] != ']':#找到reply,id结束的位置 
            num = num + 1
        messageid = int(cq[13:num])
        msg_text = f"你发的是回复\n被回复的消息id为-{messageid}\n即将撤回"#可以根据需求注释或修改回复
        await bot.send(ev, msg_text)
        await bot.delete_msg(message_id=messageid)
