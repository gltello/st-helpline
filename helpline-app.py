import streamlit as st

# Define the questions and their weights
questions = [
    {
        'question': 'In which phase of the  do you feel your digital channel implementation is?',
        'topic': "IT Infrastructure",
        'weight': 0.077,
        'answers': {
            '0. Risk management plan': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: "Develop a detailed risk management plan that includes risk identification, assessment, response planning, and monitoring. Estimated time: 1 week",
                1: "**IT Infrastructure:** <br>Based on the audit results, upgrade the IT infrastructure as necessary. This could involve increasing server capacity, updating software, etc.<br>Estimated time: 2 weeks",
                2: "**IT Infrastructure:** <br>Conduct a thorough audit of the existing IT infrastructure to ensure it can support the new digital channel launch. This step is crucial in mitigating the risk early on.<br>Estimated time: 1 week",
                3: "**IT Infrastructure:** <br>Provide technical training to the team involved in managing the digital channel. They should be able to operate, maintain, and troubleshoot the new channel.<br>Estimated time: 2 weeks",
                4: "**IT Infrastructure:** <br>Despite all efforts, there may still be unforeseen problems. Having a robust contingency plan can help manage these effectively.<br>Estimated time: 1 week",
                5: "**IT Infrastructure:** <br>Implement a structured User Acceptance Testing phase where a select group of end-users try out the new digital channel before it's fully launched. Their feedback can be used to make final adjustments, ensuring the channel meets user expectations and requirements.<br>Estimated time: 2 weeks"
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'How complete is your technology stack for digital channels?',
        'topic': "Partnerships with other institutions",
        'weight': 0.098,
        'answers': {
            '0. Technology review and enhancement': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'How do you feel your fundraise strategy is  enough and steady to cover your cost short and long term?',
        'topic': "Funding",
        'weight': 0.115,
        'answers': {
            '0. Fundraising strategy development': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'To what extent your helpline maintain confidentiality and ensure the privacy of children seeking help?',
        'topic': "Security / data protection",
        'weight': 0.159,
        'answers': {
            '0. Security audit': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': "How satisfied are you with the timeliness and responsiveness of helpline services in addressing children's needs?",
        'topic': "High response time",
        'weight': 0.093,
        'answers': {
            '0. Response time monitoring': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?',
        'topic': "Multi-platform accessibilty",
        'weight': 0.089,
        'answers': {
            '0. Developing multi-platform accessibility': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'How knowledgeable are the helpline staff about the specific issues and challenges faced by children in your country?',
        'topic': "Low Customer Satisfaction",
        'weight': 0.051,
        'answers': {
            '0. Staff training programs': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?',
        'topic': "Staffed with well-trained professionals ",
        'weight': 0.161,
        'answers': {
            '0. Diversity and inclusion training': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages (by adults or peers)?',
        'topic': "Quality of communication",
        'weight': 0.067,
        'answers': {
            '0. Developmental training for staff': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    },
    {
        'question': 'How satisfied are you with the accessibility of helplines for children in terms of availability and ease of contact?',
        'topic': "Ineffective Response / Service routing",
        'weight': 0.09,
        'answers': {
            '0. 24/7 Availability initiative': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            'Africa': {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: ""
        },
            'Asia': {
                0: 'Recomendation for Asia - Question 1 - Answer 1',
                1: 'Recomendation for Asia - Question 1 - Answer 1',
                2: 'Recomendation for Asia - Question 1 - Answer 2',
                3: 'Recomendation for Asia - Question 1 - Answer 3',
                4: 'Recomendation for Asia - Question 1 - Answer 4',
                5: 'Recomendation for Asia - Question 1 - Answer 5'
            },
            'Europe': {
                0: 'Recomendation for Europe - Question 1 - Answer 1',
                1: 'Recomendation for Europe - Question 1 - Answer 1',
                2: 'Recomendation for Europe - Question 1 - Answer 2',
                3: 'Recomendation for Europe - Question 1 - Answer 3',
                4: 'Recomendation for Europe - Question 1 - Answer 4',
                5: 'Recomendation for Europe - Question 1 - Answer 5'
            },
            'North America': {
                0: 'Recomendation for North America - Question 1 - Answer 1',
                1: 'Recomendation for North America - Question 1 - Answer 1',
                2: 'Recomendation for North America - Question 1 - Answer 2',
                3: 'Recomendation for North America - Question 1 - Answer 3',
                4: 'Recomendation for North America - Question 1 - Answer 4',
                5: 'Recomendation for North America - Question 1 - Answer 5'
            },
            'South America': {
                0: 'Recomendation for South America - Question 1 - Answer 1',
                1: 'Recomendation for South America - Question 1 - Answer 1',
                2: 'Recomendation for South America - Question 1 - Answer 2',
                3: 'Recomendation for South America - Question 1 - Answer 3',
                4: 'Recomendation for South America - Question 1 - Answer 4',
                5: 'Recomendation for South America - Question 1 - Answer 5'
            },
            'Australia': {
                0: 'Recomendation for Australia - Question 1 - Answer 1',
                1: 'Recomendation for Australia - Question 1 - Answer 1',
                2: 'Recomendation for Australia - Question 1 - Answer 2',
                3: 'Recomendation for Australia - Question 1 - Answer 3',
                4: 'Recomendation for Australia - Question 1 - Answer 4',
                5: 'Recomendation for Australia - Question 1 - Answer 5'
            }
        }
    }
]

# Define the background image URL
background_image_url = 'https://example.com/background_image.jpg'

# Streamlit app layout
def home_page():
    
    st.title('Helpline Evaluation Test')
    st.markdown('#### The following test aims to evaluate how well your helpline is performing. Please follow these steps to complete the assesment')
    st.markdown('STEP 1: From the sidebar, choose your region so that the recomendations given are tailored to your location.')
    st.markdown('STEP 2: There are 10 questions to be answered from different areas of interest, each question has 6 possible answers, each response will be graded from 0 to 5, being 0 the worst and 5 the best.')
    st.markdown('STEP 3: Hit the submit button, you will get a final score from 0 to 5, being 0 the worst and 5 the best.')
    st.markdown('STEP 4: Below the score you will find tailored recomendations for each of the 10 areas of interest of the answered questions, read them to get insights.')
    st.markdown('STEP 5: From the sidebar, visit the additional resources page to find further help on the topics from this website')
    st.markdown('##### Good Luck!')

def show_africa_page():
    st.title('Africa Page')
    st.markdown("Recomendations will be tailored to Africa's Reality")

    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'Your score: {score}')

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)

def show_asia_page():
    st.title("Asia Page")
    st.markdown("Recomendations will be tailored to Asia's Reality")
    # Add content specific to Asia
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'Your score: {score}')

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                
def show_europe_page():
    st.title("Europe Page")
    st.markdown("Recomendations will be tailored to Europe's Reality")
    # Add content specific to Europe
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'Your score: {score}')

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                

def show_north_america_page():
    st.title("North America Page")
    st.markdown("Recomendations will be tailored to North America's Reality")
    # Add content specific to North America
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'Your score: {score}')

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                

def show_south_america_page():
    st.title("South America Page")
    st.markdown("Recomendations will be tailored to South America's Reality")
    # Add content specific to South America
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'Your score: {score}')

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                

def show_australia_page():
    st.title("Australia Page")
    st.markdown("Recomendations will be tailored to Australia's Reality")
    # Add content specific to Australia
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    final_score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'Your score: {score}')

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)

# Additional resources page
def additional_resources():
    
    st.title('Additional Resources')
    st.markdown('If you need additional help with the topics of this helpline evaluation, please refer to the following resources:')
                
# Run the app
if __name__ == '__main__':
    # Display page selection
    # Create the index
    st.sidebar.title("Index")
    selection = st.sidebar.radio("Select a page", ["Home Page", "Africa", "Asia", "Europe", "North America", "South America", "Australia", "Additional Resources"])

    if selection == "Africa":
        show_africa_page()
    elif selection == "Asia":
        show_asia_page()
    elif selection == "Europe":
        show_europe_page()
    elif selection == "North America":
        show_north_america_page()
    elif selection == "South America":
        show_south_america_page()
    elif selection == "Australia":
        show_australia_page()
    elif selection == "Additional Resources":
        additional_resources()
    else:
        home_page()




