import discord
import selenium
from selenium import webdriver
from discord.ext import commands
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message):
    driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
            break
        except:
            continue
    response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
    return response

client = commands.Bot(command_prefix = '!') # prefix

@client.event
async def on_ready():
  print("bot readyy")

@client.command()
async def ping(ctx):
  await ctx.send(f'pong! {round(client.latency) * 1000} ms')

@client.command()
async def chat(ctx, *, message):
  response = get_response(message)
  await ctx.send(f"{response}")

client.run("bot token here")
