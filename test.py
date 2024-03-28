import unittest
import json
from flask_app import app

class TestAlphaChanger(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_alphachanger_cyrillic_to_latin(self):
        data = {
            "context": "Ўзбекистон (расман: Ўзбекистон Республикаси, Ўзбекистон Республикаси) – Марказий Осиёнинг марказий қисмида жойлашган мамлакат. Пойтахти – Тошкент шаҳри. Давлат тили – ўзбек тили. Майдони – 448 978 км2[6]. Ҳозирда мамлакатнинг умумий аҳолиси сони 36 миллиондан ортиқ[7][8]. Пул бирлиги – сўм. Ўзбекистон Республикаси ҳудуди 12 та вилоят, Тошкент шаҳри ва Қорақалпоғистон Республикасидан иборатдир, шунингдек, у мустақил, демократик, дунёвий ва конститутсиявий давлат ҳисобланади. Ўзбекистон МДҲ, БМТ, ЙХҲТ ва СҲҲТ аъзосидир. Ўзбекистон берк ҳудудда яъни қирғоққа ега бўлмаган беш мамлакат билан, яъни: шимолдан Қозоғистон; шимоли-шарқдан Қирғизистон; жануби-шарқдан Тожикистон; жанубдан Афғонистон; ва жануби-ғарбий қисмида Туркманистон билан чегарадош.",
            "pattern": "latin"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], "Oʻzbekiston (rasman: Oʻzbekiston Respublikasi, Oʻzbekiston Respublikasi) – Markaziy Osiyoning markaziy qismida joylashgan mamlakat. Poytaxti – Toshkent shahri. Davlat tili – oʻzbek tili. Maydoni – 448 978 km2[6]. Hozirda mamlakatning umumiy aholisi soni 36 milliondan ortiq[7][8]. Pul birligi – soʻm. Oʻzbekiston Respublikasi hududi 12 ta viloyat, Toshkent shahri va Qoraqalpogʻiston Respublikasidan iboratdir, shuningdek, u mustaqil, demokratik, dunyoviy va konstitutsiyaviy davlat hisoblanadi. Oʻzbekiston MDH, BMT, YXHT va SHHT aʼzosidir. Oʻzbekiston berk hududda yaʼni qirgʻoqqa ega boʻlmagan besh mamlakat bilan, yaʼni: shimoldan Qozogʻiston; shimoli-sharqdan Qirgʻiziston; janubi-sharqdan Tojikiston; janubdan Afgʻoniston; va janubi-gʻarbiy qismida Turkmaniston bilan chegaradosh.")

    def test_alphachanger_latin_to_cyrillic(self):
        data = {
            "context": "Oʻzbekiston (rasman: Oʻzbekiston Respublikasi, Ўзбекистон Республикаси) – Markaziy Osiyoning markaziy qismida joylashgan mamlakat. Poytaxti – Toshkent shahri. Davlat tili – oʻzbek tili. Maydoni – 448 978 km2[6]. Hozirda mamlakatning umumiy aholisi soni 36 milliondan ortiq[7][8]. Pul birligi – soʻm. Oʻzbekiston Respublikasi hududi 12 ta viloyat, Toshkent shahri va Qoraqalpogʻiston Respublikasidan iboratdir, shuningdek, u mustaqil, demokratik, dunyoviy va konstitutsiyaviy davlat hisoblanadi. Oʻzbekiston MDH, BMT, YXHT va SHHT aʼzosidir. Oʻzbekiston berk hududda yaʼni qirgʻoqqa ega boʻlmagan besh mamlakat bilan, yaʼni: shimoldan Qozogʻiston; shimoli-sharqdan Qirgʻiziston; janubi-sharqdan Tojikiston; janubdan Afgʻoniston; va janubi-gʻarbiy qismida Turkmaniston bilan chegaradosh.",
            "pattern": "cyrillic"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], "Ўзбекистон (расман: Ўзбекистон Республикаси, Ўзбекистон Республикаси) – Марказий Осиёнинг марказий қисмида жойлашган мамлакат. Пойтахти – Тошкент шаҳри. Давлат тили – ўзбек тили. Майдони – 448 978 км2[6]. Ҳозирда мамлакатнинг умумий аҳолиси сони 36 миллиондан ортиқ[7][8]. Пул бирлиги – сўм. Ўзбекистон Республикаси ҳудуди 12 та вилоят, Тошкент шаҳри ва Қорақалпоғистон Республикасидан иборатдир, шунингдек, у мустақил, демократик, дунёвий ва конститутсиявий давлат ҳисобланади. Ўзбекистон МДҲ, БМТ, ЙХҲТ ва СҲҲТ аъзосидир. Ўзбекистон берк ҳудудда яъни қирғоққа ега бўлмаган беш мамлакат билан, яъни: шимолдан Қозоғистон; шимоли-шарқдан Қирғизистон; жануби-шарқдан Тожикистон; жанубдан Афғонистон; ва жануби-ғарбий қисмида Туркманистон билан чегарадош.")

    def test_invalid_input(self):
        data = {
            "context": "",
            "pattern": "cyrillic"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], "")

    def test_invalid_pattern(self):
        data = {
            "context": "Hello, World!",
            "pattern": "invalid_pattern"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()
