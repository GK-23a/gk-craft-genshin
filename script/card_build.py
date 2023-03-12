from customlog import wlog
import character_card
import json
import os

wlog(__file__, 'out/debug.log', '卡面构建开始。')

# xlsx检测
with open('json/info.json') as jsonfile:
    info = json.loads(jsonfile.read())
    try:  
        xlsx_size = info['xlsx_size']
    except:
        xlsx_size = 0
    xlsx_size_now = os.path.getsize('data/database.xlsx')
if xlsx_size_now != xlsx_size:
    wlog(__file__, 'out/debug.log', 'database.xlsx 可能发生更改。重新生成json数据文件。')
    os.system('{} {}'.format('python', 'script/json_build.py'))
    info['xlsx_size'] = xlsx_size_now
    with open('json/info.json', 'w') as jsonfile:
        json.dump(info, jsonfile, ensure_ascii=False)
    wlog(__file__, 'out/debug.log', 'json数据文件已成功生成。')
        

wlog(__file__, 'out/debug.log', '角色图像构建开始。')

# json读取
with open('json/characters.json', encoding='UTF-8') as jsonfile:
    character_data = json.loads(jsonfile.read())
wlog(__file__, 'out/debug.log', '"characters.json"读取完成。')

# 循环图像生成
for ch_id in character_data:
    ch_img = character_card.cardbuild(ch_id, character_data)
    if ch_img:
        ch_img.save('out/character_img/'+ch_id+'.png')
        wlog(__file__, 'out/debug.log', character_data[ch_id]['name'] + ' (' + ch_id + ')已保存为 "' + ch_id + '.png" 。')

wlog(__file__, 'out/debug.log', '角色图像生成已完成全部构建与保存。\n')

wlog(__file__, 'out/debug.log', '卡面构建结束。\n')