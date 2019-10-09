import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("훈민정음 읽는 중")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!문제1번"):
        await message.channel.send("문제1번:10월9일은 훈민정음 창제일이다. (영어 소문자 o나 x를 써주세요.)")
    if message.content.startswith("x"):
        await message.channel.send("문제2번:세종대왕이 훈민정음으로 펴낸 최초의 책은 무엇인가요?")
    if message.content.startswith("용비어천가"):
        await message.channel.send("문제3번:ㆆㅿㆁ의 이름을 띄어쓰기없이 쓰시오.(예:디귿니은기역)")
    if message.content.startswith("여린히읗반치음옛이응"):
        await message.channel.send("문제4번:훈민정음 모음 초출자에는 ㅡ, ㆍ, ㅣ가 있는데 이것은 무엇을 본떠 만들어 졌는 지 띄어쓰기없이 쓰시오.(예:사과바나나배)")
    if message.content.startswith("땅하늘사람"):
        await message.channel.send("[문제5~6번]:다음 글을 읽고, 물음에 답하시오.")
        await message.channel.send(file=discord.File("image1.png"))
        await message.channel.send("문제5번:다음 그림은 훈민정음 ○○○의 서문이다. ○○○에 들어갈 알맞은 말을 쓰시오.")
    if message.content.startswith("언해본"):
        await message.channel.send("문제6번:<보기>에서 위 글에 드러난 훈민정음의 창제 정신을 모두 고른 것은?"
                                   "\n(답은 숫자로 써주세요. 예:1)"
                                   "\n```"
                                   "\n<보기>"
                                   "\nㄱ. 자주 정신"
                                   "\nㄴ. 실용 정신"
                                   "\nㄷ. 협동 정신"
                                   "\nㄹ. 애민 정신"
                                   "\nㅁ. 사대 정신"
                                   "\n```")
        await message.channel.send("①ㄱ,ㄴ  ②ㄴ,ㄷ  ③ㄷ,ㄹ  ④ㄱ,ㄴ,ㄷ  ⑤ㄱ,ㄴ,ㄹ")
    if message.content.startswith("5"):
        await message.channel.send("문제7번:<보기>는 「한글맞춤법」 제30항 사이시옷 표기의 일부이다. ㉠, ㉡, ㉢에 들어갈 단어가 바르게 연결된 것은?"
                                   "\n(답을 적을 때 괄호는 빼고 적어주세요. 답 예시: 다 )"
                                   "\n```"
                                   "\n<보기>"
                                   "\n제30항 사이시옷은 다음과 같은 경우에 받치어 적는다."
                                   "\n1. 순 우리말로 된 합성어로서 앞말이 모음으로 끝난 경우"
                                   "\n(1) 뒷말의 첫소리가 된소리로 나는 것"
                                   "\n    예: 고랫재  귓밥  ㉠"
                                   "\n(2) 뒷말의 첫소리 'ㄴ,ㅁ' 앞에너 'ㄴ' 소리가 덧나는 것"
                                   "\n    예: 뒷머리  아랫마을  ㉡"
                                   "\n(3) 뒷말의 첫소리 모음 앞에서 'ㄴㄴ' 소리가 덧나는 것"
                                   "\n    예: 도리깻열  뒷윷  ㉢"
                                   "\n```"
                                   "\n``      ㉠     ㉡     ㉢"
                                   "\n(가) 못자리  멧나물  두렛일"
                                   "\n(나) 쳇바퀴  잇몸    훗일"
                                   "\n(다) 잇자국  툇마루  나뭇잎"
                                   "\n(라) 사잣밥  곗날    예삿일"
                                   "\n(마) 못자리  두렛일  멧나물``")
    if message.content.startswith("가"):
        await message.channel.send("문제8번:다음 <보기>에서 [괄호]안에 있는 것을 옳바르게 골라 순서대로 쓰시오"
                                   "\n(정답은 띄어쓰기 없이 써주세요. 정답예시: 국어수학영어)"
                                   "\n```"
                                   "\n<보기>"
                                   "\n1. 나는 [구레나룻/구렛나루]가 짧아."
                                   "\n2. 임신해서 [홀몸/홑몸]이 아니다."
                                   "\n3. 교통사고를 당해서 다리를 [절둑/쩔뚝]거린다."
                                   "\n```")
    if message.content.startswith("구레나룻홑몸쩔뚝"):
        await message.channel.send("축하드립니다. 8문제를 모두 맞추어 문화상품권 5천원권을 드립니다."
                                   "\n문화상품권 번호 : 5813-3183-7107-251583"
                                   "\n``보리차#2300``으로 당첨문자를 캡쳐해서 보내 주시면 감사하겠습니다.")



    if message.content.startswith("!도움말"):
        await message.channel.send("```"
                                   "\n설명:한글날 기념으로 문제 8개를 맞추시면 선착순 1분에게 문화상품권 5000원을 증정해드립니다."
                                   "\n------------------------------------------------"
                                   "\n유의사항:여러명이 동시에 같은 시간때에 마지막 문제를 풀어 문화상품권을 얻게 되면 모두 같은 번호이니 풀자마자 충전하는 것을 권장합니다."
                                   "\n문제 푸는 것은 세종대왕봇의 DM으로 푸는 것을 권유합니다."
                                   "\n------------------------------------------------"
                                   "\n시작방법"
                                   "\n1. 세종대왕봇의 DM에 '!문제1번'을 입력한다."
                                   "\n2. 문제1번이 출력된다."
                                   "\n3. 정답을 입력한다."
                                   "\n4. 정답이 맞으면 바로 다음문제가 출력이 되고 정답이 틀리면 아무 일도 일어나지 않습니다."
                                   "\n5. 문제8번까지 맞추시면 문화상품권 번호가 발송됩니다."
                                   "\n------------------------------------------------"
                                   "\n그럼 잘 맞추시고 문화상품권을 받기를 바랍니다."
                                   "\n모두 행복한 한글날 되세요."
                                   "\n```"
                                   "\n``버그가 있다면 보리차#2300으로 문의해주십시오.``")




client.run("NjI5MTQ5NDYzMDcxNDI0NTEz.XZc81g.DawGwZ64idQin_QCgLWfmdyjTkU")