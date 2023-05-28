<script setup>
//import { RouterView } from 'vue-router'
</script>

<template>
  <!-- <RouterView /> -->
  <div class="main">
    <header>
      <div class="block_header">
        <div class="logo">
          <img src="./assets/img/icon.png" alt="">
        </div>
        <div class="links">
          <a >О проекте</a>
          <a v-on:click="scroll_top('#recommend')" name="recommend" class="active">Подборка <br/> занятий</a>
          <a v-on:click="scroll_top('#search')" name="search">Поиск</a>
        </div>
        <div class="nav">
          <a v-on:click="is_open_lk = true">Личный кабинет</a>
        </div>
      </div>
      
    </header>

    <Recommend v-show="user" :user="user"/>

    <div class="main_block" id="search">
      <div class="search_block">
        <div class="block_filters_items">
          <div class="block_filters">
            <div class="search">
              <input type="text" placeholder="Поиск по названию занятия" v-model="string_to_search"/>
              <button v-on:click="getSearchResult()"><img src="/img/search.png"></button>
            </div>

            <div class="block_categories"><!-- 
              <button
                class="category"
                :class="
                  category.open ? 'active_filter' : category.select ?  'active' : ''
                "
                v-for="category of categories"
                :key="category.name"
                v-on:click="clickCategory(category)"
              >
                {{ ucFirst(category.name) }}
                <img 
                  src="./assets/img/free-icon-cancel.png" 
                  :style="category.select ?  'display: block;' : 'display: none'"
                  v-on:click="clearFilter(category)"
                />
              </button> -->
              <button 
                class="preset"
                v-for="preset of presets"
                :key="preset.name"
                v-on:click="preset.select = !preset.select"
                :class="preset.select ? 'active' : ''"
              >
                <div class="checkbox_filter"><div v-if="preset.select"></div></div>
                {{ ucFirst(preset.name) }}
              </button>
            </div>
            <div class="card_filters">
              <div
                class="category"
                v-for="category_main of categories"
                :key="category_main.name"
              >
                <div v-on:click="category_main.open = !category_main.open" class="category_item">
                  <img v-show="category_main.open" src="/img/main_open.png" alt="">
                  <img v-show="!category_main.open" src="/img/main_close.png" alt="">
                  {{ ucFirst(category_main.name) }}
                </div>
              
                <div v-show="category_main.open" class="filters">
                  <div
                    class="filter"
                    v-for="category of category_main.options"
                    :key="category.name"
                  >
                    <div class="main_category" v-on:click="category.open = !category.open">
                      <button
                        class="checkbox_filter"
                        :class="category.select ? 'select' : ''"
                        v-on:click="clickFilter(category)"
                      >
                        <div v-if="category.select"></div>
                      </button>
                      {{ ucFirst(category.name) }}
                      <div class="check_arrow" v-if="category.options.length">
                        <img src="./assets/img/free-icon-down-arrow-open.png" alt="" v-if="category.open" />
                        <img src="./assets/img/free-icon-down-arrow-close.png" alt="" v-else />
                      </div>
                    </div>
                    <div v-if="category.options.length && category.open" class="block_sub">
                      <div
                        class="subcategories"
                        v-for="subcategory of category.options"
                        :key="subcategory.name"
                      >
                        <div class="main_category" v-on:click="clickFilter(subcategory, category)">
                          <div
                            class="checkbox_filter"
                            :class="subcategory.select ? 'select' : ''"
                          >
                            <div v-if="subcategory.select"></div>
                          </div>
                          {{ ucFirst(subcategory.name) }}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div> 
              <button class="show_elems" v-on:click="getSearchResult()">Показать</button>
              <button class="clear" v-on:click="clearALLFilter()">Сбросить</button>
            </div>
          </div>

          <div class="block_elements" v-show="recommendations.length && !isLoad">
            <div class="element" v-for="elem of recommendations" :key="elem.id">
              <div class="block_desc">
                <div class="name">{{ ucFirst(elem.name) }}</div>
                <div class="desc" v-if="elem.description">{{ ucFirst(elem.description) }}</div>
              </div>
              
              <div class="information">
                <div class="group_times">
                  <div class="format" v-if="elem.online">Онлайн</div>
                  <div class="address" v-else>
                    <div class="area">{{ elem.region }}</div>, &nbsp;
                    <div class="adds">{{ elem.street }}</div>, &nbsp;
                    <div class="adds">{{ elem.home}}</div>
                  </div>
                  <div class="time">
                    <div>{{ getSchedule(elem.active_schedule)[0][0] }} {{ getSchedule(elem.active_schedule)[0][1] }}</div>
                    <div v-if="getSchedule(elem.active_schedule)[1]">{{ getSchedule(elem.active_schedule)[1][0] }} {{ getSchedule(elem.active_schedule)[1][1] }}</div>
                  </div>
                </div>
                <button>Записаться</button>
              </div>
            </div>
            <button class="show_more" v-if="isShowButton" v-on:click="clickShowMore()">Показать еще</button>
          </div>
          <div class="no_search" v-show="!recommendations.length && !isLoad">
            Ничего не найдено
          </div>
          <div class="no_search" v-show="isLoad">
            <div class="lds-default"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
          </div>
        </div>
      </div>
    </div>

    <LK v-if="is_open_lk" :user="user" :closeModal="closeModal" :changeUser="changeUser"/>
    <div v-if="is_open_lk" class="scrollbar"></div>
  </div>
</template>

<script>
/** ucFirst - делает первый символ заглавный. добавить везде где текст который получаю с бека */
import { defineComponent } from "vue"
import Service from "./service";
import Recommend from "./components/Recommend.vue"
import LK from "./components/LK.vue"

export default defineComponent({
  name: "App",
  data() {
    return {
      categories: [],
      presets: [],
      users: [],
      user: null,
      open_category: {
        name: "",
        options: [],
      },
      is_open_lk: false,
      scrollWidth: 20,

      recommendations: [],
      all_recommendations: [],
      showCount: 5,
      max_showCount: 5,
      string_to_search: "",

      isLoad: true
    };
  },
  components: { Recommend, LK },
  watch:{
    is_open_lk(is_new, is_old) {
      if (is_new){
        $('body').addClass('open-modal');
        $('body.open-modal').css('padding-right', this.scrollWidth + 'px')
        $('header').css('padding-right', this.scrollWidth + 'px')
      } else {
        $('body.open-modal').css('padding-right', 0 + 'px')
        $('header').css('padding-right', 0 + 'px')
        $('body').removeClass('open-modal');
      }
    }
  },
  computed: {
    isShowButton(){
      return this.showCount < this.all_recommendations.length ? true : false
    },
  },
  mounted() {
    // ширина скроллбара
    let div = document.createElement('div');
    div.style.overflowY = 'scroll';
    div.style.width = '50px';
    div.style.height = '50px';
    document.body.append(div);
    this.scrollWidth = div.offsetWidth - div.clientWidth;
    div.remove();
    $('.scrollbar').css('width', this.scrollWidth + 'px')

    // получаем категории и пользователей
    Service.getInit().then((res) => {
      let categories = [];
      for (let category of res.categories) {
        //обработка категорий
        let cat_ = {
          name: category.name,
          options: [],
          select: false,
          open: false,
        };
        if (category.options && category.options.length) {
          for (let podcat of category.options) {
            let cat = {
              name: podcat.category ? podcat.category : (podcat.full ? podcat.full : podcat),
              options: [],
              select: false,
              open: false,
            };
            if (podcat.short) cat.short = podcat.short
            if (podcat.subcategory && podcat.subcategory.length) {
              for (let subcat of podcat.subcategory) {
                let subcat_ = {
                  name: subcat,
                  select: false,
                };
                cat.options.push(subcat_);
              }
            }
            if (podcat && podcat.category !== null) cat_.options.push(cat);
          }
        }
        categories.push(cat_);
      }
      this.categories = categories;
      this.open_category = categories[0];
      this.categories[0].open = true
      this.presets = res.presets;
      this.users = res.users;
      this.user = this.users[0];

      this.getSearchResult()
      let obj = this
      $(function(){
        $(window).scroll(function(){
          obj.scroll_active()
        });
      });
    });
    let obj = this
    $('input[type="text"]').keyup(function(e){
      if(e.which === 13){
        obj.getSearchResult()
      }
    });
  },
  methods:{
    ucFirst(name){
      return typeof name == "string" ? name.charAt(0).toUpperCase() + name.slice(1) : name
    },
    getSchedule(active_schedule){
      return eval(active_schedule)
    },
    clickFilter(category, main_cat){
      category.select = !category.select
      if (category.open){
        category.open = false
      } else {
        category.open = true
      } 
      if (category.options && category.options.length && category.select){
        for (let option of category.options){
          option.select = true
        }
      } else if (category.options && category.options.length){
        // обнулить все подкатегории
        for (let option of category.options){
          option.select = false
        }
      }

      // если не выбрана хотя бы одна подкатегоря, то категория не выделяется
      
      if (main_cat && main_cat.options.find(el => el.select == false)) main_cat.select = false
      else if (main_cat) main_cat.select = true
      
      // если выбрана хотя бы одна подкатегория или категория, то выбран весь фильтр
      let check = false
      for (let opt1 of this.open_category.options){
        if (opt1.select){
          check = true;
          break
        }
        if (opt1.options && opt1.options.length && opt1.options.find(el => el.select == true)){
          check = true;
          break
        }
      }
      if (check) this.open_category.select = true
      else this.open_category.select = false
    },
    clickCategory(category){
      this.open_category.open = false
      category.open = true
      this.open_category = category

    },
    clearFilter(category){
      category.select = false
      for (let opt1 of category.options){
        if (opt1.select) opt1.select = false
        if (opt1.options && opt1.options.length){
          for (let opt2 of opt1.options){
            if (opt2.select) opt2.select = false
          }
        }
      }
    },
    clearALLFilter(){
      for (let category of this.categories){
        category.select = false
        for (let opt1 of category.options){
          if (opt1.select) opt1.select = false
          if (opt1.options && opt1.options.length){
            for (let opt2 of opt1.options){
              if (opt2.select) opt2.select = false
            }
          }
        }
      }
      for (let preset of this.presets){ preset.select = false }
      this.string_to_search = ""
      this.getSearchResult()
    },
    closeModal(){
      this.is_open_lk = false
    },
    getParams(){
      let user_id = this.user.user_id
      let string_to_search = this.string_to_search
      let presets = []
      for (let preset of this.presets){ if (preset.select) presets.push(preset) }
      let categories = []
      for (let category of this.categories){
        let r_podcats = []
        for (let podcat of category.options){
          let r_subcats = []
          for (let subcat of podcat.options){
            if (subcat.select) r_subcats.push(subcat)
          }
          let a = {
            name: podcat.name,
            options: r_subcats
          }
          if (podcat.short) {
            a.name = podcat.short
          }
          if (podcat.select || r_subcats.length) r_podcats.push(a)
        }
        categories.push({
          name: category.name,
          options: r_podcats,
        })
      }
      return {
        user_id, string_to_search, presets, categories
      }
    },
    getSearchResult(){
      this.isLoad = true
      Service.getSearchResults(this.getParams()).then((res) => {
        this.all_recommendations = res.groups
        this.showCount = this.max_showCount
        this.recommendations = this.all_recommendations.slice(0, this.showCount)
        this.isLoad = false
      })
    },
    clickShowMore(){
      this.showCount += 5;
      this.recommendations = this.all_recommendations.slice(0, this.showCount)
    },
    changeUser(isNew){
      if (isNew){
        this.user = {
          user_id: 'new'
        }
      } else {
        let id = this.user.user_id;
        do {
          const index = Math.floor(Math.random() * (this.users.length));
          this.user = this.users[index];
        } while (this.user.user_id == id);
      }
      this.getSearchResult()
    },
    scroll_active() {
      var window_top = $(window).scrollTop();
      var search_top = 860
      if (window_top > search_top) {
        $('a[name="recommend"]').removeClass("active");
        $('a[name="search"]').addClass("active");
      } else {
        $('a[name="recommend"]').addClass("active");
        $('a[name="search"]').removeClass("active");
      }

    },
    scroll_top(id){
      $('html').animate({ 
    	    scrollTop: $(id).offset().top
        }, 500 
      )
    }
  }
});
</script>