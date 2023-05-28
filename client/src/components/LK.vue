<template>
    <div class="lk_block">
        <div class="back" v-on:click="closeModal"></div>
        <div v-if="!is_new" class="modal">
            <div class="header">
                <div class="name">Вход</div>
                <button v-on:click="is_new = true">Новый пользователь</button>
                <img src="/img/new.png" alt="">
            </div>
            <div class="user_h">Текущий пользователь</div>
            <div class="user">{{ user.name ? user.name : user.user_id }}</div>
            <div class="user_h">Адрес</div>
            <div class="user"> {{ user.user_region ? ucFirst(user.user_region + ', ') : '' }} {{ user.user_district ? ucFirst(user.user_district) : '' }}</div>
            <img class="img_tooltip" src="/img/history.png" alt="" style="margin-bottom: 12px;">
            <button class="history_user" v-on:click="isModal = true">История посещения</button>
            <button class="change_user" v-on:click="clickChange">Сменить пользователя</button>
            <img class="img_tooltip" src="/img/change.png" alt="">
            <div class="info">Данный личный кабинет предназначен для демонстрации работы рекомендательной системы для различных пользователей</div>
        </div>

        <div v-if="is_new" class="modal_new_user">
            <div class="block_modal">
                <div class="info">Спасибо за регистрацию на нашем портале, теперь вам нужно пройти небольшой тест для того чтобы мы смогли порекомендовать вам занятия на основе ваших предпочтений</div>
                <div class="wrap_question">
                    <div v-if="step <= questions.length && !isLoad" class="block_questions">
                        <div class="steps">{{ step }} / {{ questions.length }}</div>
                        <div class="question">{{ questions[step-1].question }}</div>
                        <div class="options">
                            <div class="option" 
                                v-for="option of questions[step-1].options" 
                                :key="option.value"
                                v-on:click="clickOption(option)"
                                :class="option.select ? 'active' : ''"
                            >
                                {{ option.value }}
                            </div>
                        </div>
                        <button class="next_step" :disabled="!isShowButton" v-on:click="isShowButton ? clickNextStep() : void(0)">{{ step == questions.length ? 'Отправить' : 'Далее' }}</button>
                    </div>
                    <div class="no_search" v-if="isLoad" style="height: 100%;">
                        <div class="lds-default"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="isModal" class="modal_history">
                <div class="header">История посещений</div>
                <button v-on:click="isModal = false">&#215;</button>
                <div class="history">
                    <div class="history_elem" v-for="elem of history()" :key="elem">{{ ucFirst(elem) }}</div>
                </div>
        </div>
        <div v-if="isModal" class="back" style="z-index: 10;" v-on:click="isModal = false"></div>
    </div>
</template>

<script>
/** ucFirst - делает первый символ заглавный. добавить везде где текст который получаю с бека */
    import { defineComponent } from 'vue'
    import Service from "../service";

    export default defineComponent({
        name: 'LK',
        props: ['user', 'closeModal', 'changeUser'],
        components: { },
        data() {
            return {
                is_new: false,
                step: 1,
                isModal: false,
                isLoad: false,
                questions: [
                    {
                        question: "Вы предпочитаете онлайн или очный формат занятий?",
                        options: [
                            {value: 'Онлайн', code: 'онлайн',  select: false}, 
                            {value: 'Очный', code: 'очный', select: false}
                        ]
                    },
                    {
                        question: "Какие телепередачи вы смотрите ?",
                        options: [
                            {value: 'Выпуски новостей, интеллектуальные телевикторины', code: 'интеллектуальные игры', select: false}, 
                            {value: 'Документальные и исторические фильмы', code: 'история, искусство, краеведение', select: false}, 
                            {value: 'Спортивные трансляции, передачи про здоровье', code: 'офп', select: false},
                            {value: 'Интервью с интересными и успешными людьми', code: 'психология и коммуникации', select: false},
                        ]
                    },
                    {
                        question: "Какие навыки вы бы хотели освоить?",
                        options: [
                            {value: 'Уход за собой и макияж', code: 'красота и стиль', select: false}, 
                            {value: 'Интернет и гаджеты', code: 'информационные технологии', select: false}, 
                            {value: 'Иностранные языки', code: 'иностранные языки', select: false},
                            {value: 'Финансовая грамотность', code: 'финансовая и правовая грамотность, личная безопасность', select: false},
                        ]
                    },
                    {
                        question: "Какие игры вы предпочитаете?",
                        options: [
                            {value: 'Шахматы и шашки', code: 'шахматы и шашки', select: false}, 
                            {value: 'Настольные игры', code: 'настольные игры', select: false}, 
                            {value: 'Компьютерные игры', code: 'киберспорт', select: false},
                            {value: 'Спортивные игры', code: 'спортивные игры', select: false},
                        ]
                    },
                    {
                        question: "Чем бы вы позанимались в свободное время?",
                        options: [
                            {value: 'Танцы', code: 'танцы', select: false}, 
                            {value: 'Пение', code: 'пение', select: false}, 
                            {value: 'Рисование', code: 'рисование', select: false},
                            {value: 'Домоводство и садоводство', code: 'домоводство', select: false},
                        ]
                    },
                ],
            };
        },
        computed: {
            isShowButton(){
                let check = this.questions[this.step-1].options.find(el => el.select == true ? true : false)
                return check ? true : false
            }
        },
        mounted(){
        },
        methods:{
            ucFirst(name){
                return typeof name == "string" ? name.charAt(0).toUpperCase() + name.slice(1) : name
            },
            clickNextStep(){
                this.step +=1
                //если ответил на все вопросы
                if (this.step > this.questions.length) {
                    let questions = []
                    for (let elem of this.questions){
                        questions.push({
                            question: elem.question,
                            answer: elem.options.find(el => el.select == true).code
                        })
                    }
                    console.log(questions)
                    this.isLoad = true
                    Service.getCreateUser({questions}).then((res) => {
                        this.isLoad = false
                        console.log(res)
                        this.changeUser(true)
                        this.closeModal()
                    })
                }
            },
            clickChange(){
                this.changeUser()
            },
            clickOption(option){
                for (let option of this.questions[this.step-1].options){
                    option.select = false
                }
                option.select = true
            },
            history(){
                return this.user.history ? this.user.history.split(', ') : []
            }
        }
    })
</script>