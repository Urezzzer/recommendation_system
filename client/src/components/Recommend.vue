<template>
    <div class="recommend_block" id="recommend">
        <div class="recommend_header">
            <div>
                <button :class="slide == 0 ? 'active' : ''" v-on:click="slide = 0">
                    Уникальные предложения
                </button>
                <span :class="slide == 0 ? 'active' : ''" class="s_1">3</span>
            </div>
            <div>
                <button :class="slide == 1 ? 'active' : ''" v-on:click="slide = 1">
                    На основе ваших предпочтений
                </button>
                <span :class="slide == 1 ? 'active' : ''" class="s_2">{{ recommendations_main.length }}</span>
            </div>
            <div>
                <button :class="slide == 2 ? 'active' : ''" v-on:click="slide = 2">
                    Попробуйте<br/>что-то новое
                </button>
                <span :class="slide == 2 ? 'active' : ''" class="s_3">{{ recommendations.length }}</span>
            </div>
        </div>

        <div class="recommend_items">
            <div class="owl-carousel owl-loaded promo-carousel owl-theme" v-show="slide == 0" :class="slide == 0 ? 'active' : ''">
                <div class="owl-stage-outer">
                    <div class="owl-stage">
                        <div class="owl-item" v-for="elem of promo" :key="elem.desc" data-merge="1">
                            <!-- <div class="filter"></div> -->
                            <div class="recommend__item promo"  :style="'background: url(' + elem.src + ')'">
                                <div class="block_information">
                                    <div class="name">{{elem.name}} </div>
                                    <div class="desc">{{elem.desc}}</div>
                                </div>
                                <div class="block_addr_date">
                                    <div class="addr_date">
                                        <div class="addr">{{elem.online ? 'Онлайн' : elem.addr}}</div>
                                        <div class="addr">{{elem.online ? 'Заявки принимаются' : elem.addr2}}</div>
                                        <div class="date">{{elem.date}}</div>
                                    </div>
                                    
                                    <button>Подробнее</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="owl-carousel owl-loaded recommend-carousel-main owl-theme" v-show="slide == 1" :class="slide == 1 ? 'active' : ''">
                <div class="owl-stage-outer">
                    <div class="owl-stage">
                        <div class="owl-item" v-for="elem of recommendations_main" :key="elem.id" data-merge="1">
                            <div class="recommend__item"  :style="'background: url(' + (urls[elem.name] ? urls[elem.name] : '/img/logo_m.jpg') + ')'">
                                <div class="about">
                                    <div class="name"> {{ ucFirst(elem.name) }}</div>
                                    <div class="desc" v-if="elem.description">{{ ucFirst(elem.description) }}</div>
                                </div>
                                
                                <div class="information">
                                    <div class="group_time_address">
                                        <div class="address">
                                            <div class="area" v-if="elem.region">{{ ucFirst(elem.region) }}</div>
                                            <div class="adds">{{ ucFirst(elem.street + ', ' + elem.home)}}</div>
                                        </div>
                                        <div class="time">
                                            <div>{{ elem.active_schedule[0][0] }} {{ elem.active_schedule[0][1] }}</div>
                                            <div v-if="elem.active_schedule[1]">{{ elem.active_schedule[1][0] }} {{ elem.active_schedule[1][1] }}</div>
                                        </div>
                                    </div>
                                    <button>Записаться</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="owl-carousel owl-loaded recommend-carousel owl-theme" v-show="slide == 2" :class="slide == 2 ? 'active' : ''">
                <div class="owl-stage-outer">
                    <div class="owl-stage">
                        <div class="owl-item" v-for="elem of recommendations" :key="elem.id" data-merge="1">
                            <div class="recommend__item" :style="'background: url(' + (urls[elem.name] ? urls[elem.name] : '/img/logo_m.jpg') + ')'">
                                <div class="about">
                                    <div class="name"> {{ ucFirst(elem.name) }}</div>
                                    <div class="desc" v-if="elem.description">{{ ucFirst(elem.description) }}</div>
                                </div>
                                
                                <div class="information">
                                    <div class="group_time_address">
                                        <div class="address">
                                            <div class="area" v-if="elem.region">{{ ucFirst(elem.region) }}</div>
                                            <div class="adds">{{ ucFirst(elem.street + ', ' + elem.home)}}</div>
                                        </div>
                                        <div class="time">
                                            <div>{{ elem.active_schedule[0][0] }} {{ elem.active_schedule[0][1] }}</div>
                                            <div v-if="elem.active_schedule[1]">{{ elem.active_schedule[1][0] }} {{ elem.active_schedule[1][1] }}</div>
                                        </div>
                                    </div>
                                    <button>Записаться</button>
                                </div>
                            </div>
                        </div>                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { defineComponent } from 'vue'
    import Service from "../service";

    export default defineComponent({
        name: 'Recommend',
        /**если isMain == true, то это основные рекомендации, иначе это рекомендации от других пользователей*/
        props: ['user'],
        components: { },
        data() {
            return {
                recommendations_main: [],
                recommendations: [],
                slide: 1,
                owl_main: null,
                owl: null,
                promo: [
                    {
                        name: 'Мастер класс',
                        desc: 'Для участников и зрителей мастер-класса Константин Ивлев раскроет рецепт средиземноморского итальянского супа «Инь-ян», состоящего из двух видов гаспачо.',
                        addr: 'Улица Тимура Фрунзе, дом 3',
                        addr2: 'Центр московского долголетия «Хамовники»',
                        date: '23 мая 2023 г.',
                        src: '/img/mk1.png',
                        online: false,
                    },
                    {
                        name: 'Массовый заход',
                        desc: 'В рамках проекта «Московское долголетие» пройдет массовый заход по скандинавской ходьбе. Присоединиться к спортивному празднику могут все желающие горожане старшего поколения. Гостей также ждут выступления артистов творческих участников «Московского долголетия».',
                        addr: 'Ходынский бульвар, дом 10б',
                        addr2: 'Парк «Ходынское поле»',
                        date: '19 мая 2023 г.',
                        src: '/img/mk2.jpg',
                        online: false,
                    },
                    {
                        name: 'Мастер класс',
                        desc: 'Для тех, кто ищет вдохновение и хочет познакомиться с техникой создания эскизов, один из кураторов креативного проекта Денис Еремкин проведет мастер-класс о моде.',
                        addr: '',
                        date: 'до 31 мая 2023 г.',
                        src: '/img/mk3.jpg',
                        online: true,
                    },
                ],
                urls: {
                    "скандинавская ходьба": "/img/pic/skandinavskaya-hodba.jpg",
                    "здоровая спина": "/img/pic/zdorovaya-spina.jpg",
                    "садоводство": "/img/pic/sadovodstvo.jpg",
                    "гимнастика": "/img/pic/gimnastika.jpg",
                    "изо": "/img/pic/izo.jpg",
                    "ментальная арифметика": "/img/pic/mental-arifmetic.jpg",
                    "гимнастика мозга": "/img/pic/gimnastika-mozga.jpg",
                    "осваиваем мобильные устройства": "/img/pic/osvaivaem-mobilny-ustroystva.jpg",
                    "дыхательная гимнастика": "/img/pic/dihatelnaya-gimnastika.png",
                    "пилатес": "/img/pic/pilates-dlya-pozhilykh.jpg",
                    "история, культура россии": "/img/pic/istoria-kultura-rossii.jpg",
                    "автомобильная школа": "/img/pic/avtoshkola.jpg",
                    "латиноамериканские танцы": "/img/pic/latino.jpg",
                    "тренажеры": "/img/pic/trenazhery.jpg",
                    "история искусства": "/img/pic/istoriya-iskusstva.jpg",
                    "рукоделие и творчество": "/img/pic/rukodelie-i-tvorchestvo.jpg",
                    "керамика (глина, тестопластика)": "/img/pic/keramika.jpg",
                    "восточные танцы": "/img/pic/vostochnye.jpg",
                    "цигун": "/img/pic/cigun.jpg",
                    "хоровое пение": "/img/pic/horovoepenie.jpg",
                    "московский театрал": "/img/pic/mosteatral.jpg",
                    "краеведение и пешие прогулки": "/img/pic/kraevedenie-i-peshie-progulki.jpg",
                    "физкультурно-оздоровительные занятия": "/img/pic/fizozdorov.jpg",
                    "корригирующая гимнастика для глаз": "/img/pic/gimnastikadlyaglaz.jpg",
                    "правовая грамотность": "/img/pic/pravovayagramotnost.jpg",
                    "иные интеллектуальные игры": "/img/pic/inye-int-igry.jpg",
                    "адаптивная и тонизирующая гимнастика": "/img/pic/tonizirgimnastika.jpg",
                    "стрейчинг": "/img/pic/streching.jpg",
                    "психологические тренинги": "/img/pic/Psihologicheskie-treningi.jpg",
                    "бальные танцы": "/img/pic/balnie-tancy.jpg",
                    "история русского искусства": "/img/pic/istoria-russkogo-iskusstva.jpg",
                    "суставная гимнастика": "/img/pic/sustavnaya-gimnastika.jpg",
                    "география. путешествия вокруг света": "/img/pic/geografia-puteshestvie-vokrug-sveta.jpg",
                    "ландшафтный дизайн": "/img/pic/landshaftny-design.jpg",
                    "основы духовной культуры": "/img/pic/osnovy-duhovnoy-kultury.jpg",
                    "пение": "/img/pic/penie.jpg",
                }
            };
        },
        watch: {
            user(new_user, old_user){
                this.changeRecommends()
            }
        },
        mounted(){
            if (this.user) this.changeRecommends()

            $(function() {
                $('.promo-carousel').owlCarousel(
                    {
                        loop:true,
                        nav:true,
                        margin:63,
                        items: 1.6,
                        dots: true,
                        center: true,
                        merge: true,
                        navText: ['<img src="/img/left.png">', '<img src="/img/right.png">'],
                        responsive : {
                            0: {
                                items: 1.2,
                                margin:15,
                                nav:false
                            },
                            1024: {
                                items: 1.6,
                                nav:true,
                                margin:63,
                            }
                        }
                    }
                );
            })
        },
        methods: {
            ucFirst(name){
                return typeof name == "string" ? name.charAt(0).toUpperCase() + name.slice(1) : name
            },
            changeRecommends(){
                const formData = new FormData()
                formData.append('user_id', this.user.user_id)
            //получение пользовательских рекомендаций
                Service.getPersonalRecommendations(formData).then((res) => {
                    for (let elem of res){
                        elem.active_schedule = eval(elem.active_schedule)
                    }
                    this.recommendations_main = res ? res : []
                    $(function() { 
                        if (this.owl_main) this.owl_main.trigger('refresh.owl.carousel');
                        else this.owl_main =$ ('.recommend-carousel-main').owlCarousel(
                            {
                                loop:true,
                                nav:true,
                                margin:63,
                                items: 1.6,
                                dots: true,
                                center: true,
                                merge: true,
                                navText: ['<img src="/img/left.png">', '<img src="/img/right.png">'],
                                responsive : {
                                    0: {
                                        items: 1.2,
                                        margin:15,
                                        nav:false
                                    },
                                    1024: {
                                        items: 1.6,
                                        nav:true,
                                        margin:63,
                                    }
                                }
                            }
                        ); 
                    })
                })
                //getSimilarUserBasedRecommendations - Другие пользователи предпочитают
                Service.getExpandRecommendations(formData).then((res) => {
                    for (let elem of res){
                        elem.active_schedule = eval(elem.active_schedule)
                    }
                    this.recommendations = res ? res : []
                    $(function() { 
                    if (this.owl) this.owl.trigger('refresh.owl.carousel');
                    else this.owl = $('.recommend-carousel').owlCarousel(
                        {
                            loop:true,
                            nav:true,
                            margin:63,
                            items: 1.6,
                            dots: true,
                            center: true,
                            merge: true,
                            navText: ['<img src="/img/left.png">', '<img src="/img/right.png">'],
                            responsive : {
                                0: {
                                    items: 1.2,
                                    margin:15,
                                    nav:false
                                },
                                1024: {
                                    items: 1.6,
                                    nav:true,
                                    margin:63,
                                }
                            }
                        }
                    );
                    })
        
                })
            }
        }
    })
</script>