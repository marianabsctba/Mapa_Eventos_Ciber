#!/usr/bin/env python3
import json
from datetime import datetime, timezone, date, timedelta
from pathlib import Path

# Registro verificado em páginas oficiais. O workflow remove eventos encerrados
# e publica o JSON diariamente. Acrescente novos eventos seguindo o mesmo modelo.
EVENTS = [
 {"name":"SBSeg 2026","start":"2026-09-01","end":"2026-09-04","city":"Armação dos Búzios - RJ","country":"Brasil","format":"presencial","category":"Pesquisa & CTF","description":"Simpósio Brasileiro de Cibersegurança com sessões técnicas, minicursos, indústria e CTF.","url":"https://www.sbseg2026.uff.br/"},
 {"name":"CyberSecGo 2026","start":"2026-09-03","end":"2026-09-04","city":"Goiânia - GO","country":"Brasil","format":"presencial","category":"Defesa & Governança","description":"Trilhas técnica, governança e inovação para profissionais e lideranças de segurança.","url":"https://www.cybersecgo.com.br/"},
 {"name":"Billington CyberSecurity Summit","start":"2026-09-08","end":"2026-09-10","city":"Washington, DC","country":"Estados Unidos","format":"presencial","category":"Governo & Estratégia","description":"Encontro internacional focado em segurança nacional, governo e liderança cibernética.","url":"https://billingtoncybersummit.com/"},
 {"name":"Blue Team Con","start":"2026-09-10","end":"2026-09-13","city":"Chicago, IL","country":"Estados Unidos","format":"presencial","category":"Defesa","description":"Conferência dedicada a blue team, detecção, resposta e operações defensivas.","url":"https://blueteamcon.com/"},
 {"name":"Mind The Sec 2026","start":"2026-09-15","end":"2026-09-17","city":"São Paulo - SP","country":"Brasil","format":"híbrido","category":"Mercado & Técnica","description":"Grande encontro latino-americano de cybersecurity para especialistas, gestores e CISOs.","url":"https://www.mindthesec.com.br/"},
 {"name":"Cyber Security Summit Brasil","start":"2026-10-05","end":"2026-10-06","city":"São Paulo - SP","country":"Brasil","format":"presencial","category":"Executivos & CISO","description":"Lideranças de segurança, risco, tecnologia e governo discutem confiança digital e estratégia.","url":"https://cybersecuritysummit.com.br/"},
 {"name":"Futurecom 2026","start":"2026-10-06","end":"2026-10-08","city":"São Paulo - SP","country":"Brasil","format":"presencial","category":"Cloud, IA & Segurança","description":"Infraestrutura digital, cloud, segurança, soberania e regulação em um grande fórum de tecnologia.","url":"https://www.futurecom.com.br/"},
 {"name":"Black Hat Canada","start":"2026-10-06","end":"2026-10-08","city":"Toronto","country":"Canadá","format":"presencial","category":"Ofensiva & Pesquisa","description":"Briefings técnicos e pesquisa aplicada no formato internacional da Black Hat.","url":"https://www.blackhat.com/"},
 {"name":"European Cybersecurity Challenge","start":"2026-10-12","end":"2026-10-16","city":"Europa","country":"União Europeia","format":"presencial","category":"CTF & Talentos","description":"Competição europeia organizada pela ENISA para novos talentos em cibersegurança.","url":"https://ecsc.eu/"},
 {"name":"ISC2 Security Congress","start":"2026-10-19","end":"2026-10-22","city":"Nashville, TN","country":"Estados Unidos","format":"híbrido","category":"Profissionais & Carreira","description":"Conteúdo técnico e estratégico para profissionais certificados e líderes de segurança.","url":"https://www.isc2.org/congress"},
 {"name":"II CIGRE Security 2026","start":"2026-10-28","end":"2026-10-29","city":"São Paulo - SP","country":"Brasil","format":"presencial","category":"Infraestrutura Crítica","description":"Seminário técnico de cibersegurança para energia, automação e ambientes de missão crítica.","url":"https://ce-d2.cigre.org.br/"},
 {"name":"OWASP Global AppSec","start":"2026-11-03","end":"2026-11-05","city":"Estados Unidos","country":"Estados Unidos","format":"presencial","category":"AppSec","description":"Conferência global da OWASP dedicada à segurança de aplicações e software.","url":"https://owasp.org/events/"},
 {"name":"IT Summit Nacional 2026","start":"2026-11-10","end":"2026-11-10","city":"São Paulo - SP","country":"Brasil","format":"presencial","category":"TI & Cibersegurança","description":"Encontro B2B para líderes e especialistas de tecnologia e segurança.","url":"https://itsummit.com.br/"},
 {"name":"Black Hat Middle East & Africa","start":"2026-12-01","end":"2026-12-03","city":"Riad","country":"Arábia Saudita","format":"presencial","category":"Ofensiva & Pesquisa","description":"Conferência internacional com treinamentos, pesquisa, ferramentas e comunidade hacker.","url":"https://blackhatmea.com/"}
]

def main():
    cutoff = date.today() - timedelta(days=1)
    future = []
    for event in EVENTS:
        ending = date.fromisoformat(event.get("end") or event["start"])
        if ending >= cutoff:
            item = dict(event)
            item["status"] = "CONFIRMADO"
            future.append(item)
    payload = {"updated_at": datetime.now(timezone.utc).isoformat(), "events": sorted(future, key=lambda x: x["start"])}
    out = Path("data/events.json"); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Publicados {len(future)} eventos futuros")

if __name__ == "__main__": main()
