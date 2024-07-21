import disnake
from disnake import *
from disnake.ext import commands
import json

with open("config.json") as file:
    config = json.load(file)
    owner = config['owner'] 
    hiperseguidoreskey = config['hiperseguidoreskey']
    mercadopagokey = config['mercadopagokey']
    canalLogs = config['canalLogs']
    canalCompras = config['canalCompras']

with open("valores.json") as file:
    valor = json.load(file)
    valores = valor['valores']
    valoresPor1SeguidorCurtida = valor['valoresPor1SeguidorCurtida']

class EditarHiperSeguidores(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Nova Key",
                custom_id="hiperseguidoreskey",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Editar Hiper Seguidores", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        new_key = inter.text_values["hiperseguidoreskey"]
        
        with open("config.json", "r") as file:
            config_data = json.load(file)
            config_data["hiperseguidoreskey"] = new_key

        with open("config.json", "w") as file:
            json.dump(config_data, file, indent=4)
        
        await inter.response.send_message("✅ A key **Hiper Seguidores** foi trocada com sucesso!", ephemeral=True)

class EditarMercadoPago(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Nova Key",
                custom_id="mercadopagokey",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Editar Mercado Pago", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        new_key = inter.text_values["mercadopagokey"]
        
        with open("config.json", "r") as file:
            config_data = json.load(file)
            config_data["mercadopagokey"] = new_key

        with open("config.json", "w") as file:
            json.dump(config_data, file, indent=4)

        await inter.response.send_message("✅ A key **Mercado Pago** foi trocada com sucesso!", ephemeral=True)

class EditarSeguidoresInstagram(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Novo valor",
                custom_id="novovalor",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Editar Seguidores Instagram", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        novo_valor = float(inter.text_values["novovalor"])
        
        with open("valores.json", "r") as file:
            config_data = json.load(file)

        config_data["valores"]["instagram_seguidores"] = novo_valor
        config_data["valoresPor1SeguidorCurtida"]["instagram_seguidores"] = novo_valor / 1000

        with open("valores.json", "w") as file:
            json.dump(config_data, file, indent=4)

        await inter.response.send_message("✅ O valor foi trocado com sucesso!", ephemeral=True)

class EditarSeguidoresTiktok(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Novo valor",
                custom_id="novovalor",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Editar Seguidores Tiktok", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        novo_valor = float(inter.text_values["novovalor"])
        
        with open("valores.json", "r") as file:
            config_data = json.load(file)

        config_data["valores"]["tiktok_seguidores"] = novo_valor
        config_data["valoresPor1SeguidorCurtida"]["tiktok_seguidores"] = novo_valor / 1000

        with open("valores.json", "w") as file:
            json.dump(config_data, file, indent=4)

        await inter.response.send_message("✅ O valor foi trocado com sucesso!", ephemeral=True)

class EditarCurtidasInstagram(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Novo valor",
                custom_id="novovalor",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Editar Curtidas Instagram", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        novo_valor = float(inter.text_values["novovalor"])
        
        with open("valores.json", "r") as file:
            config_data = json.load(file)

        config_data["valores"]["instagram_curtidas"] = novo_valor
        config_data["valoresPor1SeguidorCurtida"]["instagram_curtidas"] = novo_valor / 1000

        with open("valores.json", "w") as file:
            json.dump(config_data, file, indent=4)

        await inter.response.send_message("✅ O valor foi trocado com sucesso!", ephemeral=True)

class EditarCurtidasInstagram(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Novo valor",
                custom_id="novovalor",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Editar Curtidas Tiktok", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        novo_valor = float(inter.text_values["novovalor"])
        
        with open("valores.json", "r") as file:
            config_data = json.load(file)

        config_data["valores"]["tiktok_curtidas"] = novo_valor
        config_data["valoresPor1SeguidorCurtida"]["tiktok_curtidas"] = novo_valor / 1000

        with open("valores.json", "w") as file:
            json.dump(config_data, file, indent=4)

        await inter.response.send_message("✅ O valor foi trocado com sucesso!", ephemeral=True)

class Botconfig(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def botconfig(self, inter):
        """
        [👷] Configurar as funcionabilidades do Bot
        """

        if int(inter.user.id) == int(owner):
            embed = disnake.Embed(
                title="Configurar Bot | Vendas de seguidores",
                description=f"""
\👋 Olá {inter.user.mention}! Seja bem-vindo ao painel de configuração do bot de vendas de seguidores
\🔎 Explore entre as categorias abaixo para configurar/customizar o bot
            """
            )

            components=[
                disnake.ui.StringSelect(
                    custom_id="botconfig_select",
                    options=[
                        disnake.SelectOption(label="Configurar Valores", emoji="💵", value="configvalor"),
                        disnake.SelectOption(label="Configurar Canais de Logs", emoji="🚧", value="logschannels"),
                        disnake.SelectOption(label="Configurar Chaves APIS", emoji="🗝️", value="apikeys"),
                    ],
                )
            ],

            await inter.response.send_message(embed=embed, components=components, ephemeral=True)

        else: pass # ele só vai ignorar o comando de qualquer random

    @commands.Cog.listener("on_dropdown")
    async def botconfig_dropdown(self, inter):
        if inter.values[0] == "configvalor":
            components=[
                disnake.ui.StringSelect(
                    custom_id="editar_servicos",
                    placeholder="Selecione o serviço que deseja editar os valores",
                    options=[
                        disnake.SelectOption(label="Seguidores Instagram", description=f"Valor Atual: {valores['instagram_seguidores']} | Valor no Site: 1.98", value="editarseguidores_instagram"),
                        disnake.SelectOption(label="Seguidores Tiktok", description=f"Valor Atual: {valores['tiktok_seguidores']} | Valor no Site: 9.75", value="editarseguidores_tiktok"),
                        disnake.SelectOption(label="Curtidas Instagram", description=f"Valor Atual: {valores['instagram_curtidas']} | Valor no Site: 0.17", value="editarcurtidas_instagram"),
                        disnake.SelectOption(label="Curtidas Tiktok", description=f"Valor Atual: {valores['tiktok_curtidas']} | Valor no Site: 1.98", value="editarcurtidas_tiktok"),
                        disnake.SelectOption(label="Voltar", emoji="↩️", value="voltarpag_inicial"),
                    ],
                ),
            ],
            await inter.response.edit_message(components=components)
        
        elif inter.values[0] == "logschannels":
            components=[
                disnake.ui.StringSelect(
                    custom_id="editar_canais",
                    placeholder="Selecione o tipo de canal que deseja editar",
                    options=[
                        disnake.SelectOption(label="Canal de Logs", value="editarcanal_logs"),
                        disnake.SelectOption(label="Canal de Compras", value="editarcanal_compras"),
                        disnake.SelectOption(label="Voltar", emoji="↩️", value="voltarpag_inicial"),
                    ],
                ),
            ],
            await inter.response.edit_message(components=components)
    
        elif inter.values[0] == "apikeys":
            components=[
                disnake.ui.StringSelect(
                    custom_id="editar_keys",
                    placeholder="Selecione o tipo de key que deseja editar",
                    options=[
                        disnake.SelectOption(label="Hiper Seguidores", value="editar_hiperseguidores"),
                        disnake.SelectOption(label="Mercado Pago", value="editar_accesstoken"),
                        disnake.SelectOption(label="Voltar", emoji="↩️", value="voltarpag_inicial"),
                    ],
                ),
            ],
            await inter.response.edit_message(components=components)

    @commands.Cog.listener("on_dropdown")
    async def voltarpag_dropdown(self, inter):
        if inter.values[0].startswith("voltarpag"):
            pagina = inter.values[0].replace("voltarpag_", "")

            if pagina == "inicial":
                components=[
                    disnake.ui.StringSelect(
                        options=[
                            disnake.SelectOption(label="Configurar Valores", emoji="💵", value="configvalor"),
                            disnake.SelectOption(label="Configurar Canais de Logs", emoji="🚧", value="logschannels"),
                            disnake.SelectOption(label="Configurar Chaves APIS", emoji="🔑", value="apikeys"),
                        ],
                    )
                ],
                await inter.response.edit_message("", components=components)
        
            elif pagina == "canais":
                components=[
                    disnake.ui.StringSelect(
                        placeholder="Selecione o tipo de canal que deseja editar",
                        options=[
                            disnake.SelectOption(label="Canal de Logs", value="editarcanal_logs"),
                            disnake.SelectOption(label="Canal de Compras", value="editarcanal_compras"),
                            disnake.SelectOption(label="Voltar", emoji="↩️", value="voltarpag_inicial"),
                        ],
                    ),
                ],
                await inter.response.edit_message(components=components)
    
    @commands.Cog.listener("on_dropdown")
    async def editar_dropdown(self, inter):
        if inter.values[0] == "editar_hiperseguidores": await inter.response.send_modal(modal=EditarHiperSeguidores())
        elif inter.values[0] == "editar_accesstoken": await inter.response.send_modal(modal=EditarMercadoPago())

        elif inter.values[0] == "editarcanal_logs":
            components=[
                disnake.ui.ChannelSelect(
                    channel_types=[disnake.ChannelType.text],
                    custom_id="editar_canaisLogs",
                    placeholder="Selecione o novo canal de Logs",
                ),
            ],
            await inter.response.edit_message(components=components)

        elif inter.component.custom_id == "editar_canaisLogs":
            with open('config.json') as config:
                dadosServer = json.load(config)
                dadosServer["canalLogs"] = str(inter.values[0])

            with open("config.json", "w") as json_file:
                json.dump(dadosServer, json_file, indent=4)    
            
            components=[
                disnake.ui.StringSelect(
                    placeholder="Selecione o tipo de canal que deseja editar",
                    options=[
                        disnake.SelectOption(label="Canal de Logs", value="editarcanal_logs"),
                        disnake.SelectOption(label="Canal de Compras", value="editarcanal_compras"),
                        disnake.SelectOption(label="Voltar", emoji="↩️", value="voltarpag_inicial"),
                    ],
                ),
            ],
            await inter.response.edit_message(components=components)

        elif inter.values[0] == "editarcanal_compras":
            components=[
                disnake.ui.ChannelSelect(
                    channel_types=[disnake.ChannelType.text],
                    custom_id="editar_canaisCompras",
                    placeholder="Selecione o novo canal de Logs",
                ),
            ],
            await inter.response.edit_message(components=components)

        elif inter.component.custom_id == "editar_canaisCompras":
            with open('config.json') as config:
                dadosServer = json.load(config)
                dadosServer["canalCompras"] = str(inter.values[0])

            with open("config.json", "w") as json_file:
                json.dump(dadosServer, json_file, indent=4)
            
            components=[
                disnake.ui.StringSelect(
                    placeholder="Selecione o tipo de canal que deseja editar",
                    options=[
                        disnake.SelectOption(label="Canal de Logs", value="editarcanal_logs"),
                        disnake.SelectOption(label="Canal de Compras", value="editarcanal_compras"),
                        disnake.SelectOption(label="Voltar", emoji="↩️", value="voltarpag_inicial"),
                    ],
                ),
            ],
            await inter.response.edit_message(components=components)

        elif inter.values[0] == "editarseguidores_instagram": await inter.response.send_modal(modal=EditarSeguidoresInstagram())
        elif inter.values[0] == "editarseguidores_tiktok": await inter.response.send_modal(modal=EditarSeguidoresTiktok())
        elif inter.values[0] == "editarcurtidas_instagram": await inter.response.send_modal(modal=EditarCurtidasInstagram())
        elif inter.values[0] == "editarcurtidas_tiktok": await inter.response.send_modal(modal=EditarCurtidasInstagram())

def setup(bot: commands.Bot):
    bot.add_cog(Botconfig(bot))