#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itchatmp

itchatmp.update_config(itchatmp.WechatConfig(
    token='hello2018',
    appId = 'wx1f1d5a54a37112401',
    appSecret = '9a1eac4f7c6f8e284e102247a8f877691'))

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    return msg['Content']

itchatmp.run(port=5000)

