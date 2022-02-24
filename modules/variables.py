'''Hashtag Media Module.

This module holds hashtags used on twitter by news outlets,
so that they can be excluded from searches that use hashtags
in query.
'''

hashtag_media = [
       'g1', 'uolentrevista', 'globonews', 'uolnews', 'portalig', 'news',
       'bot', 'panfleterobot', 'jornaldacultura', 'jn', 'aprizion',
       'breakingnews', 'breaking_news', 'odia', 'noarnacbn', 'canaisglobo',
       'aovivo', 'urgente', 'política', 'politica', 'bandjornalismo',
       'notíciaatual', 'rodaviva', 'uol', 'msnbrasil', 'nexoexpresso', 'r7',
       'noticias', 'conexaoglobonews', 'estudioi', 'meme', 'exclusivo',
       'informação', 'jornalismo', 'edicao18', 'notícia',
       '15minutosgazetadopovo', 'rádiopampa', 'jornaldarecord', 'novodia',
       'pnbonline', 'cnn', 'rádio', 'jornaldagazeta', 'faroldabahia',
       'factchecking', 'blogtuliolemos', 'conexãoglobonews',
       'ariquemesonline', 'tuneinbrasil', 'bnews', 'notícias', 'opopular',
       'jr24h', 'edicao16', 'ofuxiqueiro', 'jornalnacional', 'empauta', 'jg',
       'bandnewsfm', 'cnnbrasil', 'uoldebate', '3em1', 'bbb21', 'capadodia',
       'bbb101', 'fantástico', 'fantastico', 'opiniaonoar', 'redepampa',
       'jornalpiracicabano', 'braincast', 'breaking', 'manhãbandeirantes',
       'copaamericanosbt', 'gnewsemponto', 'olimpiadasnaglobo',
       'fatosdasemana', 'coluna', 'shorts', 'primeirocafe', 'tênisnaespn',
       'df1', 'j10', 'papodepolítica', 'conversacombiaemau', 'podcast',
       'infojurid', 'conjur', 'redetvt', 'ficaadica', 'freecodefridaycontest',
       'avidadagente', 'bandnews20anos', 'bandnews', 'd24am', 'bandnewstv',
       'sbtnews', 'bandnews20anos', 'interagindocomanotícia', 'últimasnotícias',
       'opiniãooeste', 'tvjustica', 'falabrasil', 'jornaldaband', 'democracianoar',
       'ndmais', 'colunach', 'diariodopoder', 'credibilidade', 'loki', 'babaolmak',
       'olimpiadastokio2020', 'tokyo2020', 'pintoawards', 'rabaawards7', 'redepress',
       'jr1', 'globonews25anos', 'mourabrasilnabandnewsfm', 'salvesalvebandnews', 'felipemourabrasil',
       'jornaldamanha', 'ospingosnosis', 'tecnohour', 'diáriosemanal', 'bandnoticias',
       'jornaldacnn', 'thevoicekids', 'globonewsnuncadesliga', 'tvcultura', 'manoamano',
       'cnnnovodia', 'hnt', 'livecnnbrasil', 'acessolivre', 'materia', 'artigo', 'cnndomingo',
       'ostrêspoderes', 'f', 'cnnbrasil360', 'estúdioi', 'rádiopt', 'direitosnarede', 'redeptribeirao',
       'portalr7', 'globoplay', 'entretenimento', 'notíciastf', 'radiojustica', 'rádiogaúcha', 'gaúchaatualidade',
       'novoestadaoimpresso', 'veja', 'biroscanews', 'portaldozacaria', 'oassunto', 'g1rn', 'agita40',
       'afazenda', 'kpop', 'anime'
]

week_list = [
       # {
       #        'week_number': 1,
       #        'week_start': '2021-04-25',
       #        'deponents': {}
       # },
       #  {
       #         'week_number': 2,
       #         'week_start': '2021-05-02',
       #         'deponents': {
       #                'day_3': ['Luiz Henrique Mandetta'],
       #                'day_4': ['Eduardo Pazuello (did not attend)', 'Nelson Teich'],
       #                'day_5': ['Marcelo Queiroga']
       #         }
       #  },
       # {
       #        'week_number': 3,
       #        'week_start': '2021-05-09',
       #        'deponents': {
       #               'day_3': ['Antonio Barra Torres'],
       #               'day_4': ['Fábio Wajngarten'],
       #               'day_5': ['Carlos Murillo']  
       #        }
       # },
       # {
       #        'week_number': 4,
       #        'week_start': '2021-05-16',
       #        'deponents': {
       #               'day_3': ['Ernesto Araújo'],
       #               'day_4': ['Eduardo Pazuello'],
       #               'day_5': ['Eduardo Pazuello']  
       #        }
       # },
       # {
       #        'week_number': 5,
       #        'week_start': '2021-05-23',
       #        'deponents': {
       #               'day_3': ['Mayra Pinheiro'],
       #               'day_5': ['Dimas Covas']  
       #        }
       # },
       # {
       #        'week_number': 6,
       #        'week_start': '2021-05-30',
       #        'deponents': {
       #               'day_3': ['Nise Yamaguchi'],
       #               'day_4': ['Luana Araújo'] 
       #        }
       # },
       # {
       #        'week_number': 7,
       #        'week_start': '2021-06-06',
       #        'deponents': {
       #               'day_3': ['Marcelo Queiroga'],
       #               'day_4': ['Élcio Franco'],
       #               'day_5': ['Wilson Lima'],
       #               'day_6': ['Natalia Pasternak', 'Cláudio Maierovitch']  
       #        }
       # },
       # {
       #        'week_number': 8,
       #        'week_start': '2021-06-13',
       #        'deponents': {
       #               'day_3': ['Marcellus Campelo'],
       #               'day_4': ['Wilson witzel'],
       #               'day_5': ['Carlos Wizard (did not attend)', 'Alexandre Marques'],
       #               'day_6': ['Ricardo Ariel', 'Francisco Eduardo']  
       #        }
       # },
       # {
       #        'week_number': 9,
       #        'week_start': '2021-06-20',
       #        'deponents': {
       #               'day_3': ['Osmar Terra'],
       #               'day_4': ['Francisco Emerson'],
       #               'day_5': ['Jurema Werneck', 'Pedro Hallal'],
       #               'day_6': ['Luis Miranda', 'Luís Ricardo']  
       #        }
       # },
       # {
       #        'week_number': 10,
       #        'week_start': '2021-06-27',
       #        'deponents': {
       #               'day_3': ['Fausto Junior'],
       #               'day_4': ['Carlos Wizard'],
       #               'day_5': ['Francisco Emerson (did not attend)', 'Luiz Paulo Dominghetti'] 
       #        }
       # },
       # {
       #        'week_number': 11,
       #        'week_start': '2021-07-04',
       #        'deponents': {
       #               'day_3': ['Regina Célia'],
       #               'day_4': ['Roberto Dias'],
       #               'day_5': ['Francieli Fantinato'],
       #               'day_6': ['William Santana'] 
       #        }
       # },
       # {
       #        'week_number': 12,
       #        'week_start': '2021-07-11',
       #        'deponents': {
       #               'day_3': ['Emanuela Medrades'],
       #               'day_4': ['Emanuela Medrades'],
       #               'day_5': ['Cristiano Carvalho'] 
       #        }
       # },
       # {
       #        'week_number': 'pr_01',
       #        'week_start': '2021-07-18',
       #        'deponents': {}
       # },
       # {
       #        'week_number': 'pr_02',
       #        'week_start': '2021-07-25',
       #        'deponents': {}
       # },
       # {
       #        'week_number': 13,
       #        'week_start': '2021-08-01',
       #        'deponents': {
       #               'day_3': ['Amilton Gomes de Paula'],
       #               'day_4': ['Marcelo Blanco'],
       #               'day_5': ['Airton Antônio Soligo'] 
       #        }
       # },
       # {
       #        'week_number': 14,
       #        'week_start': '2021-08-08',
       #        'deponents': {
       #               'day_3': ['Hélcio Bruno de Almeida'],
       #               'day_4': ['Jailton Batista'],
       #               'day_5': ['Ricardo Barros'] 
       #        }
       # },
       # {
       #        'week_number': 15,
       #        'week_start': '2021-08-15',
       #        'deponents': {
       #               'day_3': ['Alexandre Costa Marques'],
       #               'day_4': ['Túlio Silveira'],
       #               'day_5': ['Francisco Maximiano'] 
       #        }
       # },
       # {
       #        'week_number': 16,
       #        'week_start': '2021-08-22',
       #        'deponents': {
       #               'day_3': ['Emanuel Cartori'],
       #               'day_4': ['Roberto Pereira Ramos Jr'],
       #               'day_5': ['josé Ricardo Santana']
       #        }
       # },
       # {
       #        'week_number': 17,
       #        'week_start': '2021-08-29',
       #        'deponents': {
       #               'day_4': ['Ivanildo Gonçalves'],
       #               'day_5': ['Francisco Araújo'] 
       #        }
       # },
       # {
       #        'week_number': 'pr_03',
       #        'week_start' : '2021-09-05',
       #        'deponents': {}
       # },
       # {
       #        'week_number': 18,
       #        'week_start': '2021-09-12',
       #        'deponents': {
       #               'day_3': ['Marcos Tolentino'],
       #               'day_4': ['Marconny Faria']
       #        }
       # }
       # {
       #        'week_number': 19,
       #        'week_start': '2021-09-19',
       #        'deponents': {
       #               'day_3': ['Wagner Rosário'],
       #               'day_4': ['Pedro Benedito'],
       #               'day_5': ['Danilo Trento']
       #        }
       # },
       # {
       #        'week_number': 20,
       #        'week_start': '2021-09-26',
       #        'deponents': {
       #               'day_3': ['Bruna Morato'],
       #               'day_4': ['Luciano Hang'],
       #               'day_5': ['Otávio Fakhoury']
       #        }
       # }
       #{
       #       'week_number': 21,
       #       'week_start': '2021-10-03',
       #       'deponents': {
       #              'day_3': ['Raimundo Nonato Basil'],
       #              'day_5': ['Paulo Rebeiro Filho'],
       #              'day_6': ['Walter Correa de Souza Netto', 'Tadeu Frederico Andrade']
       #       },
       #{
       #'week_number': 'pr_04',
       #       'week_start': '2021-10-10',
       #       'deponents': {}
       #},
       {
              'week_number': 22,
              'week_start': '2021-10-17',
              'deponents': {
                     'day_3': ['Elton da Silva Chaves']
              }
       }
]
