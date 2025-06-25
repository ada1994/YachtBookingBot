from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import logging

# 启用日志记录
logging.basicConfig(level=logging.DEBUG)

# 设置游艇信息字典
yacht_sizes = {
    "38ft 双体快艇👨‍👩‍👧‍👦20人": "https://t.me/youtingbaby/122", 
    "39ft 快艇Speedboat👨‍👩‍👧‍👦20人": "https://t.me/youtingbaby/115", 
    "39ft 钓鱼艇 ‍👩‍👧‍👦12人": "https://t.me/youtingbaby/109", 
    "42ft 双体Yacht👨‍👩‍👧‍👦10人": "https://t.me/youtingbaby/40?single", 
    "42ft 德宏Yacht👨‍👩‍👧‍👦12人": "https://t.me/youtingbaby/71", 
    "54ft Azimut👨‍👩‍👧‍👦15人": "https://t.me/youtingbaby/30",
    "62ft 星瑞Sease‍👩‍👧‍👦19人": "https://t.me/youtingbaby/107",
    "63ft Sea-Stella👨‍👩‍👧‍👦19人": "https://t.me/youtingbaby/102",
    "63ft JF游艇👨‍👩‍👧‍👦20人": "https://t.me/youtingbaby/158",
    "65ft JP👨‍👩‍👧‍👦19人": "https://t.me/youtingbaby/89",
    "95尺 ZH游艇👨‍👩‍👧‍👦50人": "https://t.me/youtingbaby/150",
    "95ft 水神Aquitalia👨‍👩‍👧‍👦50人": "https://t.me/youtingbaby/69"
}

async def start(update: Update, context):
    # 打印调试信息
    logging.debug("Received /start command")

    # 创建每排两个按钮的布局
    keyboard = [
        [InlineKeyboardButton(size, url=url) for size, url in list(yacht_sizes.items())[i:i+2]]  # 每排2个按钮
        for i in range(0, len(yacht_sizes), 2)  # 按照每2个为一组，分成不同的行
    ]
    
    # 添加下方的两行按钮
    keyboard.append([InlineKeyboardButton("✈ 联系客服 Cust Serv", url='https://t.me/Boatbabes')])
    keyboard.append([InlineKeyboardButton("📅 在线预订", callback_data='book_now')])

    # 使用 InlineKeyboardMarkup 来格式化为按钮布局
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 拼接消息文本
    message_text = (
        "🤖 **西港游艇服务**\n"
        "Sihanoukville Yacht Booking\n\n"
        "🛥 提供豪华游艇租赁服务，42尺至95尺可选\n"
        "Luxury yacht rentals from 42ft to 95ft\n\n"
        "🚤 <b>游艇尺寸 & 载客限制</b>\n\n"
        
        "<a href='https://t.me/youtingbaby/28'>DJ宝贝定制服务</a>\n"
        "<a href='https://t.me/youtingbaby/122'>38ft快艇Speedboat👨‍👩‍👧‍👦20人</a>\n"
        "<a href='https://t.me/youtingbaby/115'>39ft快艇Speedboat👨‍👩‍👧‍👦20人 350$/趟</a>\n"
        "<a href='https://t.me/youtingbaby/109'>39ft钓鱼艇Fishing Boat👨‍👩‍👧‍👦12人 1000$起</a>\n"
        "<a href='https://t.me/youtingbaby/40?single'>42ft双体游艇👨‍👩‍👧‍👦12人 $1280</a>\n"
        "<a href='https://t.me/youtingbaby/71'>42ft德宏‍👩‍👧‍👦10人 1600$</a>\n"
        "<a href='https://t.me/youtingbaby/30'>54ft 意大利Azimut👨‍👩‍👧‍👦15人 1800$</a>\n"
        "<a href='https://t.me/youtingbaby/107'>62ft 星瑞Sease👨‍👩‍👧‍👦19人 2800$</a>\n"
        "<a href='https://t.me/youtingbaby/102'>63ft Sea-Stella👨‍👩‍👧‍👦19人 2500$</a>\n"
        "<a href='https://t.me/youtingbaby/158'>63ft JF游艇👨‍👩‍👧‍👦20人 2200$</a>\n"
        "<a href='https://t.me/youtingbaby/89'>65ft JP游艇👨‍👩‍👧‍👦19人 2600$</a>\n"
        "<a href='https://t.me/youtingbaby/69'>95ft 水神Aquitalia👨‍👩‍👧‍👦50人 4500$</a>\n"
        "<a href='https://t.me/youtingbaby/150'>95ft ZH忠恒👨‍👩‍👧‍50人 5500$</a>\n\n"

                
        
        "⏰ 出海时间：09:00 – 17:00\n"
        "📍 航线：西港码头 – 高龙岛 / 撒冷岛\n"
        "Route: Koh Rong / Koh Rong Sanloem\n"
        "📲 支持中文 & English 服务\n\n"
        
        "🎉 <b>自费服务内容：</b>\n"
        "DJ宝贝｜水上项目｜深潜浮潜｜摩托艇｜山地车｜岛上食宿\n"
        "Boat Babes | Water Sports | Diving & Snorkeling | Jet Ski | ATV | Island Stay & Meals\n\n"
        
        "📩 预订请点击菜单或联系人工客服 👉 @Boatbabes\n"
        "Click the menu or contact live support 👉 @Boatbabes"
    )

    # 发送消息
    await update.message.reply_text(
        message_text,
        reply_markup=reply_markup,
        parse_mode="HTML",
        disable_web_page_preview=True
    )


# 启动应用
def main():
    # 创建 Application 对象
    application = Application.builder().token("8034425757:AAGsRVp13yopy38n6NVap9Re9zIl7oMcYpw").build()  # 替换为你的 Bot API token

    # 添加处理器
    application.add_handler(CommandHandler("start", start))

    # 启动机器人
    logging.debug("Starting bot...")
    application.run_polling()

if __name__ == "__main__":
    main()
