# pessoal sei que muitos estão com dificuldade de encontrar os emojis, então vou lista-los aqui para
# ficar mais fácil de acha-los com a ferramenta de bucar e altera-los, além disso, coloquei os emojis dentro de uma pasta daqui
# <:giveaway:1221134296660574229>
# <:email:1221134302180413532>
# <:atention:1221134598709444761>
# <:cart:1221134323550261279>
# <:person:1221134285914902538>
# <:yes:1221134312150274108>
# <:rocket:1221134550982332437>
# <:no:1221134309507862589>
# <:continue:1221136270613282826>
# <:tiktok:1260786934897311814>
# <:insta:1260785188456370188>
# <:enviar:1210717523176194088>
# <:maisblank:1208229995953262592>
# <:menosblank:1208520674864529458>
# <a:b_no:1208231246870618182>
# <:carrinho:1210937081585467402>
# <:clock:1221134291396726786>
# <:papel:1221098043647066142>
# <:cargosGuild:1223094240972640359>
# <:pixLogo:1221163563830214808>


import disnake
from disnake.ext import commands
import json
import asyncio
import mercadopago
import requests
from datetime import datetime
import os
from disnake import *
from io import BytesIO

nomes = {
    "instagram_seguidores": "Seguidores ・ Instagram",
    "tiktok_seguidores": "Seguidores ・ Tiktok",
    "instagram_curtidas": "Curtidas・ Instagram",
    "tiktok_curtidas": "Curtidas ・ Tiktok"
}

MODEL_CHOICES = [
    "Embed",
    "Mensagem"
]

with open("config.json") as file:
    config = json.load(file)
    owner = config['owner'] 
    hiperseguidoreskey = config['hiperseguidoreskey']
    mercadopagokey = config['mercadopagokey']
    logsCanal = config['canalLogs']
    comprasCanal = config['canalCompras']

with open("valores.json") as file:
    valor = json.load(file)
    valores = valor['valores']
    valoresPor1SeguidorCurtida = valor['valoresPor1SeguidorCurtida']

sdk = mercadopago.SDK(mercadopagokey)
request_options = mercadopago.config.RequestOptions()

###############################################################################################################################################################################

async def enviar_servico(tipo_serivco, quantidade, link, inter):
    if tipo_serivco == "instagram_seguidores":
        api_url = "https://hiperseguidores.com.br/api/v2"
        order_data = {
            'key': hiperseguidoreskey,
            'action': 'add',
            'service': 4,
            'link': link,
            'quantity': int(quantidade),
        }
        response = requests.post(api_url, data=order_data)
        response_json = response.json()
        
        order = response_json.get("order")
        embed = disnake.Embed(description=f"# <:giveaway:1221134296660574229> Pedido finalizado com sucesso\nSeu pedido foi concluido e os seguidores já estão indo para sua conta. Caso tenha algum problema, contate nossa equipe de suporte.\nLembre-se de que o pedido pode levar até 24 horas para ser completo.")
        embedLogs= disnake.Embed(description=f"# <:email:1221134302180413532> Recibo do pedido ・ {inter.user.id} | {inter.user.name}\n- **Link da conta**: {link}\n- **Quantidade de seguidores**: ``{quantidade}``\n- **Order ID**: ``{order}``")
        
        await inter.user.send(f"Se os seguidores não forem enviados, entre em contato com o suporte e envie os seguintes detalhes:\n**Order ID:** `{order}`\n**Link da conta:** {link}\n**Quantidade de seguidores:** `{quantidade}`", embed=embed)
        
        await inter.response.defer()
        await inter.channel.purge(limit=100)
        await inter.channel.send("# Seu pedido foi confirmado e já está sendo enviado\nOlhe sua DM para ter mais informações sobre seu pedido! Este carrinho vai fechar em **20 segundos**")
        
        logs = inter.guild.get_channel(logsCanal)
        await logs.send(embed=embedLogs)
        
        await asyncio.sleep(20)
        await inter.channel.delete()

    elif tipo_serivco == "tiktok_seguidores":
        api_url = "https://hiperseguidores.com.br/api/v2"
        order_data = {
            'key': hiperseguidoreskey,
            'action': 'add',
            'service': 103,
            'link': link,
            'quantity': int(quantidade),
        }
        response = requests.post(api_url, data=order_data)
        response_json = response.json()
        order = response_json.get("order")

        embed = disnake.Embed(description=f"# <:giveaway:1221134296660574229> Pedido finalizado com sucesso\nSeu pedido foi concluido e os seguidores já estão indo para sua conta. Caso tenha algum problema, contate nossa equipe de suporte.\nLembre-se de que o pedido pode levar até 24 horas para ser completo.")
        embedLogs= disnake.Embed(description=f"# <:email:1221134302180413532> Recibo do pedido ・ {inter.user.id} | {inter.user.name}\n- **Link da conta**: {link}\n- **Quantidade de seguidores**: ``{quantidade}``\n- **Order ID**: ``{order}``")
        
        await inter.user.send(f"Se os seguidores não forem enviados, entre em contato com o suporte e envie os seguintes detalhes:\n**Order ID:** `{order}`\n**Link da conta:** {link}\n**Quantidade de seguidores:** `{quantidade}`", embed=embed)
        
        await inter.response.defer()
        await inter.channel.purge(limit=100)
        
        await inter.channel.send("# Seu pedido foi confirmado e já está sendo enviado\nOlhe sua DM para ter mais informações sobre seu pedido! Este carrinho vai fechar em **20 segundos**")
        
        logs = inter.guild.get_channel(logsCanal)
        await logs.send(embed=embedLogs)
        
        await asyncio.sleep(20)
        await inter.channel.delete()
    
    elif tipo_serivco == "instagram_curtidas":
        api_url = "https://hiperseguidores.com.br/api/v2"
        order_data = {
            'key': hiperseguidoreskey,
            'action': 'add',
            'service': 125,
            'link': link,
            'quantity': int(quantidade),
        }
        response = requests.post(api_url, data=order_data)
        response_json = response.json()
        order = response_json.get("order")

        embed = disnake.Embed(description=f"# <:giveaway:1221134296660574229> Pedido finalizado com sucesso\nSeu pedido foi concluido e as curtidas já estão indo para sua conta. Caso tenha algum problema, contate nossa equipe de suporte.\nLembre-se de que o pedido pode levar até 24 horas para ser completo.")
        embedLogs= disnake.Embed(description=f"# <:email:1221134302180413532> Recibo do pedido ・ {inter.user.id} | {inter.user.name}\n- **Link da conta**: {link}\n- **Quantidade de curtidas**: ``{quantidade}``\n- **Order ID**: ``{order}``")
        
        await inter.user.send(f"Se as curtidas não forem enviadas dentro de 24 horas, entre em contato com o suporte e envie os seguintes detalhes:\n**Order ID:** `{order}`\n**Link da conta:** {link}\n**Quantidade de curtidas:** `{quantidade}`", embed=embed)
        
        await inter.response.defer()
        await inter.channel.purge(limit=100)
        
        await inter.channel.send("# Seu pedido foi confirmado e já está sendo enviado\nOlhe sua DM para ter mais informações sobre seu pedido! Este carrinho vai fechar em **20 segundos**")
        
        logs = inter.guild.get_channel(logsCanal)
        await logs.send(embed=embedLogs)
        
        await asyncio.sleep(20)
        await inter.channel.delete()

    elif tipo_serivco == "tiktok_curtidas":
        api_url = "https://hiperseguidores.com.br/api/v2"
        order_data = {
            'key': hiperseguidoreskey,
            'action': 'add',
            'service': 44,
            'link': link,
            'quantity': int(quantidade),
        }
        response = requests.post(api_url, data=order_data)
        response_json = response.json()
        order = response_json.get("order")

        embed = disnake.Embed(description=f"# <:giveaway:1221134296660574229> Pedido finalizado com sucesso\nSeu pedido foi concluido e as curtidas já estão indo para sua conta. Caso tenha algum problema, contate nossa equipe de suporte.\nLembre-se de que o pedido pode levar até 24 horas para ser completo.")
        embedLogs= disnake.Embed(description=f"# <:email:1221134302180413532> Recibo do pedido ・ {inter.user.id} | {inter.user.name}\n- **Link da conta**: {link}\n- **Quantidade de curtidas**: ``{quantidade}``\n- **Order ID**: ``{order}``")
        
        await inter.user.send(f"Se as curtidas não forem enviadas dentro de 24 horas, entre em contato com o suporte e envie os seguintes detalhes:\n**Order ID:** `{order}`\n**Link da conta:** {link}\n**Quantidade de curtidas:** `{quantidade}`", embed=embed)
        
        await inter.response.defer()
        await inter.channel.purge(limit=100)
        
        await inter.channel.send("# Seu pedido foi confirmado e já está sendo enviado\nOlhe sua DM para ter mais informações sobre seu pedido! Este carrinho vai fechar em **20 segundos**")
        
        logs = inter.guild.get_channel(logsCanal)
        await logs.send(embed=embedLogs)
        
        await asyncio.sleep(20)
        await inter.channel.delete()

###############################################################################################################################################################################

class EnviarSeguidoresInstagram(disnake.ui.Modal):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        components = [
            disnake.ui.TextInput(
                label="Link da conta (obrigatório ser pública)",
                placeholder="https://www.instagram.com/...",
                custom_id="linkconta",
                style=TextInputStyle.short,
                max_length=1000,
            ),
            disnake.ui.TextInput(
                label="Você confirma que a conta é válida e pública?",
                placeholder="Confirmo",
                custom_id="confirmation",
                style=TextInputStyle.short,
                max_length=8,
                min_length=8
            ),
        ]
        super().__init__(title="Enviar Seguidores ・ Instagram", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        link_conta = inter.text_values.get("linkconta")
        confirmation = inter.text_values.get("confirmation")

        if confirmation.lower() != "confirmo":
            await inter.response.send_message("<:atention:1221134598709444761> Você não confirmou que a conta é pública e válida. Tente novamente!", ephemeral=True)
        else:
            await enviar_servico(tipo_serivco="instagram_seguidores", quantidade=self.quantidade, link=link_conta, inter=inter)
            
class EnviarSeguidoresTiktok(disnake.ui.Modal):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        components = [
            disnake.ui.TextInput(
                label="Link da conta (obrigatório ser pública)",
                placeholder="https://www.tiktok.com/...",
                custom_id="linkconta",
                style=TextInputStyle.short,
                max_length=1000,
            ),
            disnake.ui.TextInput(
                label="Você confirma que a conta é válida e pública?",
                placeholder="Confirmo",
                custom_id="confirmation",
                style=TextInputStyle.short,
                max_length=8,
                min_length=8
            ),
        ]
        super().__init__(title="Enviar Seguidores ・ Tiktok", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        link_conta = inter.text_values.get("linkconta")
        confirmation = inter.text_values.get("confirmation")

        if confirmation.lower() != "confirmo":
            await inter.response.send_message("<:atention:1221134598709444761> Você não confirmou que a conta é pública e válida. Tente novamente!", ephemeral=True)
        else:
            await enviar_servico(tipo_serivco="tiktok_seguidores", quantidade=self.quantidade, link=link_conta, inter=inter)

class EnviarCurtidasInstagram(disnake.ui.Modal):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        components = [
            disnake.ui.TextInput(
                label="Link da conta (obrigatório ser pública)",
                placeholder="https://www.instagram.com/...",
                custom_id="linkconta",
                style=TextInputStyle.short,
                max_length=1000,
            ),
            disnake.ui.TextInput(
                label="Você confirma que a conta é válida e pública?",
                placeholder="Confirmo",
                custom_id="confirmation",
                style=TextInputStyle.short,
                max_length=8,
                min_length=8
            ),
        ]
        super().__init__(title="Enviar Curtidas ・ Instagram", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        link_conta = inter.text_values.get("linkconta")
        confirmation = inter.text_values.get("confirmation")

        if confirmation.lower() != "confirmo":
            await inter.response.send_message("<:atention:1221134598709444761> Você não confirmou que a conta é pública e válida. Tente novamente!", ephemeral=True)
        else:
            await enviar_servico(tipo_serivco="instagram_curtidas", quantidade=self.quantidade, link=link_conta, inter=inter)

class EnviarCurtidasTiktok(disnake.ui.Modal):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        components = [
            disnake.ui.TextInput(
                label="Link da conta (obrigatório ser pública)",
                placeholder="https://www.tiktok.com/...",
                custom_id="linkconta",
                style=TextInputStyle.short,
                max_length=1000,
            ),
            disnake.ui.TextInput(
                label="Você confirma que a conta é válida e pública?",
                placeholder="Confirmo",
                custom_id="confirmation",
                style=TextInputStyle.short,
                max_length=8,
                min_length=8
            ),
        ]
        super().__init__(title="Enviar Curtidas ・ Tiktok", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        link_conta = inter.text_values.get("linkconta")
        confirmation = inter.text_values.get("confirmation")

        if confirmation.lower() != "confirmo":
            await inter.response.send_message("<:atention:1221134598709444761> Você não confirmou que a conta é pública e válida. Tente novamente!", ephemeral=True)
        else:
            await enviar_servico(tipo_serivco="tiktok_curtidas", quantidade=self.quantidade, link=link_conta, inter=inter)

###############################################################################################################################################################################

async def existe_carrinho_aberto(channel, service_name):
    for thread in channel.threads:
        if service_name in thread.name:
            return True, thread.jump_url

    return False, None

###############################################################################################################################################################################

def criar_pagamento(valor):
    payment_data = {
        "transaction_amount": valor,
        "payment_method_id": "pix",
        "payer": {
            "email": "hiperseguidores@firemail.com.br"
        }
    }

    payment_response = sdk.payment().create(payment_data, request_options)
    payment = payment_response["response"]

    if "id" in payment:
        payment_id = payment["id"]

    if "point_of_interaction" in payment:
        qr_code = payment["point_of_interaction"]["transaction_data"]["qr_code"]
    else:
        qr_code = "Erro ao criar o pagamento"

    url = "https://api.qrcode-monkey.com//qr/custom"
    payload = {
        "data":str(qr_code),
        "config": {
            "body":"round",
            "eye":"frame2",
            "eyeBall":"ball14",
            "erf1":["fv"],
            "erf2":[],
            "erf3":[],
            "brf1":[],
            "brf2":[],
            "brf3":[],
            "bodyColor":"#C67717",
            "bgColor":"#FFFFFF",
            "eye1Color":"#C67717",
            "eye2Color":"#C67717",
            "eye3Color":"#C67717",
            "eyeBall1Color":"#C67717",
            "eyeBall2Color":"#C67717",
            "eyeBall3Color":"#C67717",
            "gradientColor1":"",
            "gradientColor2":"",
            "gradientType":"linear",
            "gradientOnEyes":"true",
            "logo":None,
            "logoMode":"default"
            },
            "size":2000,
            "download":"imageUrl",
            "file":"png"}
    response = requests.request("POST", url, json=payload)
    response = response.json()
    qr_code_response = response['imageUrl']
    copia_e_cola = qr_code
    return qr_code_response, copia_e_cola, payment_id

async def registrar_db(inter, produto_comprado):
    filename = f"db/{inter.user.id}.json"
    nova_data = str(datetime.now())

    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_data = json.load(file)
        
        if "servico_comprado" in existing_data:
            if produto_comprado in existing_data["servico_comprado"]:
                existing_data["servico_comprado"][produto_comprado].append(nova_data)
            else:
                existing_data["servico_comprado"][produto_comprado] = [nova_data]
        else:
            existing_data["servico_comprado"] = {produto_comprado: [nova_data]}
        

        existing_data["nome"] = inter.user.name
        existing_data["id"] = inter.user.id
        
        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)
    else:
        data = {
            "servico_comprado": {
                produto_comprado: [nova_data]
            },
            "nome": inter.user.name,
            "id": inter.user.id
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    
    return

###############################################################################################################################################################################

async def verificar_status_pagamento(payment_id, channel, inter, tipo_de_servico, quantidade_servico, valor):
    while True:
        payment_info_response = sdk.payment().get(payment_id)
        payment_info = payment_info_response["response"]
        
        if payment_info["status"] == "approved":

            async for message in channel.history():
                await message.delete()

            compras = inter.guild.get_channel(comprasCanal)
            logs = inter.guild.get_channel(logsCanal)

            embed = disnake.Embed(description="# <:cart:1221134323550261279> Compra aprovada")
            embed.add_field(name="Pagamento feito por:", value=f"{inter.user.mention}", inline=True)
            embed.add_field(name="Valor pago:", value=f"``R${valor}``", inline=True)
            embed.add_field(name="Quantidade:", value=f"``{quantidade_servico}``", inline=True)
            embed.add_field(name="Serviço:", value=f"``1x {nomes[f'{tipo_de_servico}']}``", inline=False)
            embed.set_footer(text=f"{inter.guild.name} ・ Pedido feito por {inter.user.name}", icon_url=inter.user.avatar.url)

            await logs.send(embed=embed)
            await compras.send(embed=embed)
            await registrar_db(inter, tipo_de_servico)

            if tipo_de_servico == "instagram_seguidores":
                embed = disnake.Embed(
                    title="<:giveaway:1221134296660574229> Pagamento aprovado ・ Instagram Seguidores",
                    description=f"""
<:yes:1221134312150274108> Seu pagamento foi aprovado com sucesso
<:cart:1221134323550261279> **Valor pago**: {valor}
<:rocket:1221134550982332437> **Tipo de serviço**: Seguidores ・ Instagram
<:person:1221134285914902538> **Quantidade de seguidores**: {quantidade_servico} seguidores
                    """
                )
                button = disnake.ui.Button(label="Enviar Seguidores", style=disnake.ButtonStyle.blurple, emoji="<:rocket:1221134550982332437>", custom_id=f"enviarSeguidoresInstagram_{quantidade_servico}")
                await channel.send(embed=embed, components=button)
 
            elif tipo_de_servico == "tiktok_seguidores":
                embed = disnake.Embed(
                    title="<:giveaway:1221134296660574229> Pagamento aprovado ・ Tiktok Seguidores",
                    description=f"""
<:yes:1221134312150274108> Seu pagamento foi aprovado com sucesso
<:cart:1221134323550261279> **Valor pago**: {valor}
<:rocket:1221134550982332437> **Tipo de serviço**: Seguidores ・ Tiktok
<:person:1221134285914902538> **Quantidade de seguidores**: {quantidade_servico} seguidores
                    """
                )
                button = disnake.ui.Button(label="Enviar Seguidores", style=disnake.ButtonStyle.blurple, emoji="<:rocket:1221134550982332437>", custom_id=f"enviarSeguidoresTiktok_{quantidade_servico}")
                await channel.send(embed=embed, components=button)

            elif tipo_de_servico == "instagram_curtidas":
                embed = disnake.Embed(
                    title="<:giveaway:1221134296660574229> Pagamento aprovado ・ Instagram Curtidas",
                    description=f"""
<:yes:1221134312150274108> Seu pagamento foi aprovado com sucesso
<:cart:1221134323550261279> **Valor pago**: {valor}
<:rocket:1221134550982332437> **Tipo de serviço**: Curtidas ・ Instagram
<:person:1221134285914902538> **Quantidade de curtidas**: {quantidade_servico} curtidas
                    """
                )
                button = disnake.ui.Button(label="Enviar Curtidas", style=disnake.ButtonStyle.blurple, emoji="<:rocket:1221134550982332437>", custom_id=f"enviarCurtidasInstagram_{quantidade_servico}")
                await channel.send(embed=embed, components=button)

            elif tipo_de_servico == "tiktok_curtidas":
                embed = disnake.Embed(
                    title="<:giveaway:1221134296660574229> Pagamento aprovado ・ Tiktok Curtidas",
                    description=f"""
<:yes:1221134312150274108> Seu pagamento foi aprovado com sucesso
<:cart:1221134323550261279> **Valor pago**: {valor}
<:rocket:1221134550982332437> **Tipo de serviço**: Curtidas ・ Tiktok
<:person:1221134285914902538> **Quantidade de curtidas**: {quantidade_servico} curtidas
                    """
                )
                button = disnake.ui.Button(label="Enviar Curtidas", style=disnake.ButtonStyle.blurple, emoji="<:rocket:1221134550982332437>", custom_id=f"enviarCurtidasTiktok_{quantidade_servico}")
                await channel.send(embed=embed, components=button)

            break
        
        await asyncio.sleep(1)

###############################################################################################################################################################################

async def mandar_msg_logs(embed, mensagem, inter):
    logs = inter.guild.get_channel(logs)

    if embed: await logs.send(embed=embed)
    if mensagem: await logs.send(mensagem)

class EnviarEmbedPainel(disnake.ui.Modal):
    def __init__(self, canal):
        self.canal = canal
        components = [
            disnake.ui.TextInput(
                label="Titulo da embed",
                custom_id="title",
                style=TextInputStyle.short,
                max_length=30,
            ),
            disnake.ui.TextInput(
                label="Descrição da embed",
                custom_id="description",
                style=TextInputStyle.long,
            ),
            disnake.ui.TextInput(
                label="Imagem da Embed (URL)",
                custom_id="image",
                style=TextInputStyle.short,
                required=False
            ),
        ]
        super().__init__(title="Customizar Embed ・ Painel", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        title = inter.text_values.get("title")
        description = inter.text_values.get("description")
        image = inter.text_values.get("image")

        if not image: image = None
        embed = disnake.Embed(title=title, description=description)
        embed.set_image(url=image)

        components=[
            disnake.ui.StringSelect(
                placeholder="Selecione seu serviço",
                custom_id="servicos_option",
                options=[
                    disnake.SelectOption(label="Instagram ・ Seguidores", description=f"$/Mil: R${valores['instagram_seguidores']} | Pedido min: 100", emoji="<:insta:1260785188456370188>", value="instagram_seguidores"),
                    disnake.SelectOption(label="Tiktok ・ Seguidores", description=f"$/Mil: R${valores['tiktok_seguidores']} | Pedido min: 100", emoji="<:tiktok:1260786934897311814>", value="tiktok_seguidores"),
                    disnake.SelectOption(label="Instagram ・ Curtidas", description=f"$/Mil: R${valores['instagram_curtidas']} | Pedido min: 100", emoji="<:insta:1260785188456370188>", value="instagram_curtidas"),
                    disnake.SelectOption(label="Tiktok ・ Curtidas", description=f"$/Mil: R${valores['tiktok_curtidas']} | Pedido min: 100", emoji="<:tiktok:1260786934897311814>", value="tiktok_curtidas"),
                ],
            )
        ]

        await self.canal.send(embed=embed, components=components)
        await inter.response.defer()

class EnviarMensagemPainel(disnake.ui.Modal):
    def __init__(self, canal):
        self.canal = canal
        components = [
            disnake.ui.TextInput(
                label="Mensagem",
                custom_id="message",
                style=TextInputStyle.long,
            ),
            disnake.ui.TextInput(
                label="URL da imagem",
                custom_id="url_image",
                style=TextInputStyle.short,
                required=False
            )
        ]
        super().__init__(title="Customizar Mensagem ・ Painel", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        mensagem = inter.text_values.get("message")
        image = inter.text_values.get("url_image")

        response = requests.get(image)
        image_data = BytesIO(response.content)
        image_file = disnake.File(fp=image_data, filename="image.png")

        components=[
            disnake.ui.StringSelect(
                placeholder="Selecione seu serviço",
                custom_id="servicos_option",
                options=[
                    disnake.SelectOption(label="Instagram ・ Seguidores", description=f"$/Mil: R${valores['instagram_seguidores']} | Pedido min: 100", emoji="<:insta:1260785188456370188>", value="instagram_seguidores"),
                    disnake.SelectOption(label="Tiktok ・ Seguidores", description=f"$/Mil: R${valores['tiktok_seguidores']} | Pedido min: 100", emoji="<:tiktok:1260786934897311814>", value="tiktok_seguidores"),
                    disnake.SelectOption(label="Instagram ・ Curtidas", description=f"$/Mil: R${valores['instagram_curtidas']} | Pedido min: 100", emoji="<:insta:1260785188456370188>", value="instagram_curtidas"),
                    disnake.SelectOption(label="Tiktok ・ Curtidas", description=f"$/Mil: R${valores['tiktok_curtidas']} | Pedido min: 100", emoji="<:tiktok:1260786934897311814>", value="tiktok_curtidas"),
                ],
            )
        ]

        await self.canal.send(mensagem, components=components, file=image_file)
        await inter.response.defer()

###############################################################################################################################################################################

class Painel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

###############################################################################################################################################################################
    @commands.slash_command()
    async def consultar_historico(self, inter, user: disnake.User):
        """
        [👷] Mostra o histórico de compras de um usuário especifíco

        Parameters
        ----------
        user: usuário desejado para ver o histórico
        """

        if int(inter.user.id) == int(owner):
            filename = f"db/{inter.user.id}.json"

            if os.path.exists(filename):
                embed = disnake.Embed(
                    title="<:cart:1221134323550261279> Histórico de compras",
                    description=f"Aqui está o histórico de compras do usuário {user.mention}"
                )
                embed.set_author(name=inter.user.name, icon_url=inter.user.avatar.url)
                
                with open(filename, "r") as file:
                    existing_data = json.load(file)

                for tipo_de_servico, datas_comprado in existing_data['servico_comprado'].items():
                    datas_str = "\n".join(f"<:clock:1221134291396726786> {data}" for data in datas_comprado)
                    embed.add_field(name=f"<:email:1221134302180413532> {tipo_de_servico}", value=datas_str, inline=False)
                
                await inter.response.send_message(embed=embed, ephemeral=True)
            
            else: await inter.response.send_message("<:no:1221134309507862589> Não há nenhum histórico de compras para este usuário!", ephemeral=True)

        else: await inter.response.send_message("<:no:1221134309507862589> Você não tem permissão para executar este comando!", ephemeral=True)

    @commands.slash_command()
    async def consultar_pedido(self, inter, order_id: str):
        """
        [🪪] Consultar estado do pedido
        
        Parameters
        ----------
        order_id: ID do pedido
        """
        order_data = {
            "key": hiperseguidoreskey,
            "action": "status",
            "order": order_id
        }
        response = requests.post("https://hiperseguidores.com.br/api/v2", data=order_data)
        if "status" not in response.text:
            await inter.response.send_message("<:no:1221134309507862589> Seu pedido não foi encontrado no nosso sistema, tente contatar suporte com nossa equipe!", ephemeral=True)
        else:
            await inter.response.send_message(f"<:continue:1221136270613282826> Segue informações sobre o pedido `{order_id}`:\n```json\n{response.json()}```", ephemeral=True)

    @commands.slash_command()
    async def enviar_painel(self, inter, canal: disnake.TextChannel, tipo_de_mensagem: str):
        """
        [👷] Mande o painel para o canal de comprar seguidores

        Parameters
        ----------
        canal: que canal o painel vai ser enviado?
        tipo_de_mensagem: qual vai ser o tipo da mensagem?
        """

#         mensagem = """
# Eleve o nível da sua rede social ao comprar seguidores conosco, de uma forma segura, prática e rápida!

# <:rocket:1221134550982332437> **Benefícios inclusos:**
# - **Entrega automática:** Receba seus seguidores de forma automática, sem ajuda humana
# - **Facilidade e agilidade:** Compre de maneira segura conosco e receba seu produto em questão de minutos
# - **Segurança e conforto:** Conte com nossa equipe de suporte para o que precisar e compre com segurança
# """

        if int(inter.author.id) == int(owner): 
            if tipo_de_mensagem == "Embed": await inter.response.send_modal(modal=EnviarEmbedPainel(canal=canal))
            else: await inter.response.send_modal(modal=EnviarMensagemPainel(canal=canal))
        else: await inter.response.send_message("<:no:1221134309507862589> Você não tem permissão para executar este comando!", ephemeral=True)

    @enviar_painel.autocomplete("tipo_de_mensagem")
    async def tipo_autocomp(inter: disnake.CommandInteraction, string: str):
        string = string.lower()
        return [model for model in MODEL_CHOICES if string in model.lower()]

###############################################################################################################################################################################

    @commands.Cog.listener("on_dropdown")
    async def criar_carrinho(self, inter):
        # ele verifica se já existe algum carrinho
        service_mapping = {
            "instagram_seguidores": f"Instagram Seguidores ・ {inter.user.name} | {inter.user.id}",
            "tiktok_seguidores": f"Tiktok Seguidores ・ {inter.user.name} | {inter.user.id}",
            "instagram_curtidas": f"Instagram Curtidas ・ {inter.user.name} | {inter.user.id}",
            "tiktok_curtidas": f"Tiktok Curtidas ・ {inter.user.name} | {inter.user.id}"
        }

        service_name = service_mapping.get(inter.values[0])
        carrinho_existe, jump_url = await existe_carrinho_aberto(inter.channel, service_name)     
        if carrinho_existe:
            await inter.response.send_message(f"<:no:1221134309507862589> Já existe um carrinho aberto para este serviço", ephemeral=True, components=disnake.ui.Button(label="Ir para o carrinho", emoji="<:enviar:1210717523176194088>", url=jump_url))
            return
        
        # se o carrinho não existir, ele continua com o processo de criação de carrinho

        if inter.values[0] == "instagram_seguidores":
            topico = await inter.channel.create_thread(name=f"Instagram Seguidores ・ {inter.user.name} | {inter.user.id}", type=disnake.ChannelType.private_thread, invitable=False)
            embed = disnake.Embed(
                title="<:insta:1260785188456370188> Comprar Seguidores ・ Instagram",
                description=f"""
- **Quantidade de seguidores:** 1000 seguidores
- **Quantidade minima de seguidores:** 100 seguidores
- **Valor por mil seguidores:** R${valores['instagram_seguidores']}

- **Valor final:** R${valores['instagram_seguidores']}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id="adicionarSeguidoresInstagram_1000_100"), #adicionarSeguidoresInstagram_quantidadeAtual_quantidadeParaAdicionar
                    disnake.ui.Button(disabled=True, label="1000 Seguidores"),
                    disnake.ui.Button(label=f"Valor: R${valores['instagram_seguidores']}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id="removerSeguidoresInstagram_1000_100"), #removerSeguidoresInstagram_quantidadeAtual_quantidadeParaRemover
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoInstagramSeguidores_1000_{valores['instagram_seguidores']}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await topico.send(f"{inter.user.mention}", embed=embed, components=buttons)
            await inter.response.send_message(f"<:cart:1221134323550261279> Carrinho criado com sucesso em: {topico.mention}", components=disnake.ui.Button(label="Ir para o carrinho", emoji="<:enviar:1210717523176194088>", url=topico.jump_url), ephemeral=True)

###############################################################################################################################################################################

        elif inter.values[0] == "tiktok_seguidores":
            topico = await inter.channel.create_thread(name=f"Tiktok Seguidores ・ {inter.user.name} | {inter.user.id}", type=disnake.ChannelType.private_thread, invitable=False)
            embed = disnake.Embed(
                title="<:tiktok:1260786934897311814> Comprar Seguidores ・ Tiktok",
                description=f"""
- **Quantidade de seguidores:** 1000 seguidores
- **Quantidade minima de seguidores:** 100 seguidores
- **Valor por mil seguidores:** R${valores['tiktok_seguidores']}

- **Valor final:** R${valores['tiktok_seguidores']}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id="adicionarSeguidoresTiktok_1000_100"), #adicionarSeguidoresTiktok_quantidadeAtual_quantidadeParaAdicionar
                    disnake.ui.Button(disabled=True, label="1000 Seguidores"),
                    disnake.ui.Button(label=f"Valor: R${valores['tiktok_seguidores']}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id="removerSeguidoresTiktok_1000_100"), #removerSeguidoresTiktok_quantidadeAtual_quantidadeParaRemover
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoTiktokSeguidores_1000_{valores['tiktok_seguidores']}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await topico.send(f"{inter.user.mention}", embed=embed, components=buttons)
            await inter.response.send_message(f"<:cart:1221134323550261279> Carrinho criado com sucesso em: {topico.mention}", components=disnake.ui.Button(label="Ir para o carrinho", emoji="<:enviar:1210717523176194088>", url=topico.jump_url), ephemeral=True)

###############################################################################################################################################################################

        elif inter.values[0] == "instagram_curtidas":
            topico = await inter.channel.create_thread(name=f"Instagram Curtidas ・ {inter.user.name} | {inter.user.id}", type=disnake.ChannelType.private_thread, invitable=False)
            embed = disnake.Embed(
                title="<:insta:1260785188456370188> Comprar Curtidas ・ Instagram",
                description=f"""
- **Quantidade de curtidas:** 1000 curtidas
- **Quantidade minima de curtidas:** 100 curtidas
- **Valor por mil curtidas:** R${valores['instagram_curtidas']}

- **Valor final:** R${valores['instagram_curtidas']}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id="adicionarCurtidasInstagram_1000_100"), #adicionarCurtidasInstagram_quantidadeAtual_quantidadeParaAdicionar
                    disnake.ui.Button(disabled=True, label="1000 Curtidas"),
                    disnake.ui.Button(label=f"Valor: R${valores['instagram_curtidas']}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id="removerCurtidasInstagram_1000_100"), #removerCurtidasInstagram_quantidadeAtual_quantidadeParaRemover
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoInstagramCurtidas_1000_{valores['instagram_curtidas']}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await topico.send(f"{inter.user.mention}", embed=embed, components=buttons)
            await inter.response.send_message(f"<:cart:1221134323550261279> Carrinho criado com sucesso em: {topico.mention}", components=disnake.ui.Button(label="Ir para o carrinho", emoji="<:enviar:1210717523176194088>", url=topico.jump_url), ephemeral=True)

###############################################################################################################################################################################

        elif inter.values[0] == "tiktok_curtidas":
            topico = await inter.channel.create_thread(name=f"Tiktok Curtidas ・ {inter.user.name} | {inter.user.id}", type=disnake.ChannelType.private_thread, invitable=False)
            embed = disnake.Embed(
                title="<:tiktok:1260786934897311814> Comprar Curtidas ・ Tiktok",
                description=f"""
- **Quantidade de curtidas:** 1000 curtidas
- **Quantidade minima de curtidas:** 100 curtidas
- **Valor por mil curtidas:** R${valores['tiktok_curtidas']}

- **Valor final:** R${valores['tiktok_curtidas']}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id="adicionarCurtidasTiktok_1000_100"), #adicionarCurtidasTiktok_quantidadeAtual_quantidadeParaRemover
                    disnake.ui.Button(disabled=True, label="1000 Curtidas"),
                    disnake.ui.Button(label=f"Valor: R${valores['tiktok_curtidas']}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id="removerCurtidasTiktok_1000_100"), #removerCurtidasTiktok_quantidadeAtual_quantidadeParaRemover
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoTiktokCurtidas_1000_{valores['tiktok_curtidas']}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await topico.send(f"{inter.user.mention}", embed=embed, components=buttons)
            await inter.response.send_message(f"<:cart:1221134323550261279> Carrinho criado com sucesso em: {topico.mention}", components=disnake.ui.Button(label="Ir para o carrinho", emoji="<:enviar:1210717523176194088>", url=topico.jump_url), ephemeral=True)
    
###############################################################################################################################################################################

    @commands.Cog.listener("on_button_click")
    async def apagar_carrinho(self, inter):
        if inter.component.custom_id == "apagarCarrinho":
            await inter.response.send_message("<:clock:1221134291396726786> Apagando o carrinho em alguns instantes")
            await asyncio.sleep(2)
            await inter.channel.delete()

###############################################################################################################################################################################

    @commands.Cog.listener("on_button_click")
    async def adicionar_quantidade(self, inter):
        if inter.component.custom_id.startswith("adicionarSeguidoresInstagram"):
            nome, quantitidadeAtual, quantidadeAumentar = inter.component.custom_id.split("_")
            quantidadeFinal = int(quantitidadeAtual) + int(quantidadeAumentar)
            valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['instagram_seguidores']
            valorFinal = round(valorFinal, 2)
            embed = disnake.Embed(title="<:insta:1260785188456370188> Comprar Seguidores ・ Instagram", description=f"- **Quantidade de seguidores:** {quantidadeFinal} seguidores\n- **Quantidade minima de seguidores:** 100 seguidores\n- **Valor por mil seguidores:** R${valores['instagram_seguidores']}\n\n- **Valor final:** R${valorFinal}"
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarSeguidoresInstagram_{quantidadeFinal}_100"),
                    disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Seguidores"),
                    disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerSeguidoresInstagram_{quantidadeFinal}_100"),
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoInstagramSeguidores_{quantidadeFinal}_{valorFinal}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await inter.response.edit_message(embed=embed, components=buttons)
            
        elif inter.component.custom_id.startswith("adicionarSeguidoresTiktok"):
            nome, quantitidadeAtual, quantidadeAumentar = inter.component.custom_id.split("_")
            quantidadeFinal = int(quantitidadeAtual) + int(quantidadeAumentar)
            valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['tiktok_seguidores']
            valorFinal = round(valorFinal, 2)
            embed = disnake.Embed(
                title="<:tiktok:1260786934897311814> Comprar Seguidores ・ Tiktok",
                description=f"""
- **Quantidade de seguidores:** {quantidadeFinal} seguidores
- **Quantidade minima de seguidores:** 100 seguidores
- **Valor por mil seguidores:** R${valores['tiktok_seguidores']}

- **Valor final:** R${valorFinal}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarSeguidoresTiktok_{quantidadeFinal}_100"),
                    disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Seguidores"),
                    disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerSeguidoresTiktok_{quantidadeFinal}_100"),
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoTiktokSeguidores_{quantidadeFinal}_{valorFinal}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await inter.response.edit_message(embed=embed, components=buttons)

        elif inter.component.custom_id.startswith("adicionarCurtidasInstagram"):
            nome, quantitidadeAtual, quantidadeAumentar = inter.component.custom_id.split("_")
            quantidadeFinal = int(quantitidadeAtual)+int(quantidadeAumentar)
            valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['instagram_curtidas']
            valorFinal = round(valorFinal, 2)
            embed = disnake.Embed(
                title="<:insta:1260785188456370188> Comprar Curtidas ・ Instagram",
                description=f"""
- **Quantidade de curtidas:** {quantidadeFinal} curtidas
- **Quantidade minima de curtidas:** 100 curtidas
- **Valor por mil curtidas:** R${valores['instagram_curtidas']}

- **Valor final:** R${valores['instagram_curtidas']}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarCurtidasInstagram_{quantidadeFinal}_100"),
                    disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Curtidas"),
                    disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerCurtidasInstagram_{quantidadeFinal}_100"),
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoInstagramCurtidas_{quantidadeFinal}_{valorFinal}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await inter.response.edit_message(embed=embed, components=buttons)

        elif inter.component.custom_id.startswith("adicionarCurtidasTiktok"):
            nome, quantitidadeAtual, quantidadeAumentar = inter.component.custom_id.split("_")
            quantidadeFinal = int(quantitidadeAtual)+int(quantidadeAumentar)
            valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['tiktok_curtidas']
            valorFinal = round(valorFinal, 2)
            embed = disnake.Embed(
                title="<:insta:1260785188456370188> Comprar Curtidas ・ Tiktok",
                description=f"""
- **Quantidade de curtidas:** {quantidadeFinal} curtidas
- **Quantidade minima de curtidas:** 100 curtidas
- **Valor por mil curtidas:** R${valores['tiktok_curtidas']}

- **Valor final:** R${valores['tiktok_curtidas']}
            """
            )
            buttons = [
                [
                    disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarCurtidasTiktok_{quantidadeFinal}_100"),
                    disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Curtidas"),
                    disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                    disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerCurtidasTiktok_{quantidadeFinal}_100"),
                ],
                [
                    disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoTiktokCurtidas_{quantidadeFinal}_{valorFinal}"),
                    disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                ]
            ]
            await inter.response.edit_message(embed=embed, components=buttons)

###############################################################################################################################################################################

    @commands.Cog.listener("on_button_click")
    async def remover_quatidade(self, inter):
        if inter.component.custom_id.startswith("removerSeguidoresInstagram"):
            nome, quantitidadeAtual, quantidadeDiminuir = inter.component.custom_id.split("_")
            if int(quantitidadeAtual) <= 100:
                await inter.response.defer()
            else: 
                quantidadeFinal = int(quantitidadeAtual) - int(quantidadeDiminuir)
                valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['instagram_seguidores']
                valorFinal = round(valorFinal, 2)
                embed = disnake.Embed(title="<:insta:1260785188456370188> Comprar Seguidores ・ Instagram", description=f"- **Quantidade de seguidores:** {quantidadeFinal} seguidores\n- **Quantidade minima de seguidores:** 100 seguidores\n- **Valor por mil seguidores:** R${valores['instagram_seguidores']}\n\n- **Valor final:** R${valorFinal}"
                )
                buttons = [
                    [
                        disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarSeguidoresInstagram_{quantidadeFinal}_100"),
                        disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Seguidores"),
                        disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                        disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerSeguidoresInstagram_{quantidadeFinal}_100"),
                    ],
                    [
                        disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoInstagramSeguidores_{quantidadeFinal}_{valorFinal}"),
                        disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                    ]
                ]
                await inter.response.edit_message(embed=embed, components=buttons)

        elif inter.component.custom_id.startswith("removerSeguidoresTiktok"):
            nome, quantitidadeAtual, quantidadeDiminuir = inter.component.custom_id.split("_")
            if int(quantitidadeAtual) <= 100:
                await inter.response.defer()
            else: 
                quantidadeFinal = int(quantitidadeAtual) - int(quantidadeDiminuir)
                valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['tiktok_seguidores']
                valorFinal = round(valorFinal, 2)
                embed = disnake.Embed(title="<:insta:1260785188456370188> Comprar Seguidores ・ Tiktok", description=f"- **Quantidade de seguidores:** {quantidadeFinal} seguidores\n- **Quantidade minima de seguidores:** 100 seguidores\n- **Valor por mil seguidores:** R${valores['tiktok_seguidores']}\n\n- **Valor final:** R${valorFinal}"
                )
                buttons = [
                    [
                        disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarSeguidoresTiktok_{quantidadeFinal}_100"),
                        disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Seguidores"),
                        disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                        disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerSeguidoresTiktok_{quantidadeFinal}_100"),
                    ],
                    [
                        disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoTiktokSeguidores_{quantidadeFinal}_{valorFinal}"),
                        disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                    ]
                ]
                await inter.response.edit_message(embed=embed, components=buttons)

        elif inter.component.custom_id.startswith("removerCurtidasInstagram"):
            nome, quantitidadeAtual, quantidadeDiminuir = inter.component.custom_id.split("_")
            if int(quantitidadeAtual) <= 100:
                await inter.response.defer()
            else: 
                quantidadeFinal = int(quantitidadeAtual) - int(quantidadeDiminuir)
                valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['instagram_curtidas']
                valorFinal = round(valorFinal, 2)
                embed = disnake.Embed(title="<:insta:1260785188456370188> Comprar Curtidas ・ Instagram", description=f"- **Quantidade de curtidas:** {quantidadeFinal} curtidas\n- **Quantidade minima de curtidas:** 100 curtidas\n- **Valor por mil curtidas:** R${valores['instagram_curtidas']}\n\n- **Valor final:** R${valorFinal}"
                )
                buttons = [
                    [
                        disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarCurtidasInstagram_{quantidadeFinal}_100"),
                        disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Curtidas"),
                        disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                        disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerCurtidasInstagram_{quantidadeFinal}_100"),
                    ],
                    [
                        disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoCurtidasInstagram_{quantidadeFinal}_{valorFinal}"),
                        disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                    ]
                ]
                await inter.response.edit_message(embed=embed, components=buttons)

        elif inter.component.custom_id.startswith("removerCurtidasTiktok"):
            nome, quantitidadeAtual, quantidadeDiminuir = inter.component.custom_id.split("_")
            if int(quantitidadeAtual) <= 100:
                await inter.response.defer()
            else: 
                quantidadeFinal = int(quantitidadeAtual) - int(quantidadeDiminuir)
                valorFinal = quantidadeFinal * valoresPor1SeguidorCurtida['tiktok_curtidas']
                valorFinal = round(valorFinal, 2)
                embed = disnake.Embed(title="<:insta:1260785188456370188> Comprar Curtidas ・ Tiktok", description=f"- **Quantidade de curtidas:** {quantidadeFinal} curtidas\n- **Quantidade minima de curtidas:** 100 curtidas\n- **Valor por mil curtidas:** R${valores['tiktok_curtidas']}\n\n- **Valor final:** R${valorFinal}"
                )
                buttons = [
                    [
                        disnake.ui.Button(emoji="<:maisblank:1208229995953262592>", custom_id=f"adicionarCurtidasTiktok_{quantidadeFinal}_100"),
                        disnake.ui.Button(disabled=True, label=f"{quantidadeFinal} Curtidas"),
                        disnake.ui.Button(label=f"Valor: R${valorFinal}", disabled=True),
                        disnake.ui.Button(emoji="<:menosblank:1208520674864529458>", custom_id=f"removerCurtidasTiktok_{quantidadeFinal}_100"),
                    ],
                    [
                        disnake.ui.Button(emoji="<:carrinho:1210937081585467402>", label="Continuar para pagamento", style=disnake.ButtonStyle.green, custom_id=f"pagamentoCurtidasTiktok_{quantidadeFinal}_{valorFinal}"),
                        disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido"),
                    ]
                ]
                await inter.response.edit_message(embed=embed, components=buttons)

###############################################################################################################################################################################

    @commands.Cog.listener("on_button_click")
    async def criar_pagamento(self, inter):
        global copia_e_cola
        if inter.component.custom_id.startswith("pagamentoInstagramSeguidores"):
            nome, quantidadeSeguidores, valorFinal = inter.component.custom_id.split("_")
            valorFinal = float(valorFinal)
            quantidadeSeguidores = int(quantidadeSeguidores)

            await inter.channel.purge(limit=2)
            msg = await inter.channel.send("<a:Loading_branco:1211379073650008105> Aguarde enquanto processamos seu pedido")
            
            qr_code_response, copia_e_cola, payment_id = criar_pagamento(valorFinal)
            qr_code_response = qr_code_response.replace(r"\/\/", "")
            qr_code_response = qr_code_response.replace("//", "")
            qr_code_response = f"https://{qr_code_response}"

            embed = disnake.Embed(
                title="<:carrinho:1210937081585467402> Pagamento ・ Seguidores Instagram",
                description=f"""
🪙 **Valor final**: R${valorFinal}
<:cargosGuild:1223094240972640359> **Quantidade de seguidores**: {quantidadeSeguidores} seguidores
<:pixLogo:1221163563830214808> **Código copia e cola**:
```{copia_e_cola}```
"""
            )
            embed.set_image(url=qr_code_response)

            botoes = [
                disnake.ui.Button(label="Copiar Copia e Cola", custom_id=f"copiaecola", emoji="<:papel:1221098043647066142>"),
                disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido")
            ]

            await msg.delete()
            await inter.channel.send(embed=embed, components=botoes)
            asyncio.create_task(verificar_status_pagamento(payment_id, inter.channel, inter, "instagram_seguidores", quantidadeSeguidores, valorFinal))

        elif inter.component.custom_id.startswith("pagamentoTiktokSeguidores"):
            nome, quantidadeSeguidores, valorFinal = inter.component.custom_id.split("_")
            valorFinal = float(valorFinal)
            quantidadeSeguidores = int(quantidadeSeguidores)

            await inter.channel.purge(limit=2)
            msg = await inter.channel.send("<a:Loading_branco:1211379073650008105> Aguarde enquanto processamos seu pedido")
            
            qr_code_response, copia_e_cola, payment_id = criar_pagamento(valorFinal)
            qr_code_response = qr_code_response.replace(r"\/\/", "")
            qr_code_response = qr_code_response.replace("//", "")
            qr_code_response = f"https://{qr_code_response}"

            embed = disnake.Embed(
                title="<:carrinho:1210937081585467402> Pagamento ・ Seguidores Tiktok",
                description=f"""
🪙 **Valor final**: R${valorFinal}
<:cargosGuild:1223094240972640359> **Quantidade de seguidores**: {quantidadeSeguidores} seguidores
<:pixLogo:1221163563830214808> **Código copia e cola**:
```{copia_e_cola}```
"""
            )
            embed.set_image(url=qr_code_response)

            botoes = [
                disnake.ui.Button(label="Copiar Copia e Cola", custom_id=f"copiaecola", emoji="<:papel:1221098043647066142>"),
                disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido")
            ]

            await msg.delete()
            await inter.channel.send(embed=embed, components=botoes)
            asyncio.create_task(verificar_status_pagamento(payment_id, inter.channel, inter, "tiktok_seguidores", quantidadeSeguidores, valorFinal))

        elif inter.component.custom_id.startswith("pagamentoCurtidasInstagram"):
            nome, quantidadeCurtidas, valorFinal = inter.component.custom_id.split("_")
            valorFinal = float(valorFinal)
            quantidadeCurtidas = int(quantidadeCurtidas)

            await inter.channel.purge(limit=2)
            msg = await inter.channel.send("<a:Loading_branco:1211379073650008105> Aguarde enquanto processamos seu pedido")
            
            qr_code_response, copia_e_cola, payment_id = criar_pagamento(valorFinal)
            qr_code_response = qr_code_response.replace(r"\/\/", "")
            qr_code_response = qr_code_response.replace("//", "")
            qr_code_response = f"https://{qr_code_response}"

            embed = disnake.Embed(
                title="<:carrinho:1210937081585467402> Pagamento ・ Curtidas Instagram",
                description=f"""
🪙 **Valor final**: R${valorFinal}
<:cargosGuild:1223094240972640359> **Quantidade de curtidas**: {quantidadeCurtidas} curtidas
<:pixLogo:1221163563830214808> **Código copia e cola**:
```{copia_e_cola}```
"""
            )
            embed.set_image(url=qr_code_response)

            botoes = [
                disnake.ui.Button(label="Copiar Copia e Cola", custom_id=f"copiaecola", emoji="<:papel:1221098043647066142>"),
                disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido")
            ]

            await msg.delete()
            await inter.channel.send(embed=embed, components=botoes)
            asyncio.create_task(verificar_status_pagamento(payment_id, inter.channel, inter, "instagram_curtidas", quantidadeCurtidas, valorFinal))

        elif inter.component.custom_id.startswith("pagamentoCurtidasTiktok"):
            nome, quantidadeCurtidas, valorFinal = inter.component.custom_id.split("_")
            valorFinal = float(valorFinal)
            quantidadeCurtidas = int(quantidadeCurtidas)

            await inter.channel.purge(limit=2)
            msg = await inter.channel.send("<a:Loading_branco:1211379073650008105> Aguarde enquanto processamos seu pedido")
            
            qr_code_response, copia_e_cola, payment_id = criar_pagamento(valorFinal)
            qr_code_response = qr_code_response.replace(r"\/\/", "")
            qr_code_response = qr_code_response.replace("//", "")
            qr_code_response = f"https://{qr_code_response}"

            embed = disnake.Embed(
                title="<:carrinho:1210937081585467402> Pagamento ・ Curtidas Tiktok",
                description=f"""
🪙 **Valor final**: R${valorFinal}
<:cargosGuild:1223094240972640359> **Quantidade de curtidas**: {quantidadeCurtidas} curtidas
<:pixLogo:1221163563830214808> **Código copia e cola**:
```{copia_e_cola}```
"""
            )
            embed.set_image(url=qr_code_response)

            botoes = [
                disnake.ui.Button(label="Copiar Copia e Cola", custom_id=f"copiaecola", emoji="<:papel:1221098043647066142>"),
                disnake.ui.Button(emoji="<a:b_no:1208231246870618182>", custom_id="apagarCarrinho", style=disnake.ButtonStyle.red, label="Cancelar pedido")
            ]

            await msg.delete()
            await inter.channel.send(embed=embed, components=botoes)
            asyncio.create_task(verificar_status_pagamento(payment_id, inter.channel, inter, "tiktok_curtidas", quantidadeCurtidas, valorFinal))

###############################################################################################################################################################################

        elif inter.component.custom_id.startswith("copiaecola"):
            await inter.response.send_message(copia_e_cola, ephemeral=True)
        
        elif inter.component.custom_id.startswith("enviarSeguidoresInstagram"):
            quantidade = int(inter.component.custom_id.replace("enviarSeguidoresInstagram_", ""))
            await inter.response.send_modal(modal=EnviarSeguidoresInstagram(quantidade))

        elif inter.component.custom_id.startswith("enviarSeguidoresTiktok"):
            quantidade = int(inter.component.custom_id.replace("enviarSeguidoresTiktok_", ""))
            await inter.response.send_modal(modal=EnviarSeguidoresTiktok(quantidade))

        elif inter.component.custom_id.startswith("enviarCurtidasInstagram"):
            quantidade = int(inter.component.custom_id.replace("enviarCurtidasInstagram_", ""))
            await inter.response.send_modal(modal=EnviarCurtidasInstagram(quantidade))

        elif inter.component.custom_id.startswith("enviarCurtidasTiktok"):
            quantidade = int(inter.component.custom_id.replace("enviarCurtidasTiktok_", ""))
            await inter.response.send_modal(modal=EnviarCurtidasTiktok(quantidade))
            
###############################################################################################################################################################################

def setup(bot: commands.Bot):
    bot.add_cog(Painel(bot))