  'use strict'
/**
 * 페이지 스크롤에 따른 요소 제어
 */
// 페이지 스크롤에 영향을 받는 요소들을 검색!
const badgeEl = document.querySelector('header .badges')
const toTopEl = document.querySelector('#to-top')
// 페이지에 스크롤 이벤트를 추가!
// 스크롤이 지나치게 자주 발생하는 것을 조절(throttle, 일부러 부하를 줌)
window.addEventListener('scroll', _.throttle(function () {
  // 페이지 스크롤 위치가 500px이 넘으면.
  if (window.scrollY > 500) {
    // Badge 요소 숨기기!
    gsap.to(badgeEl, .6, {
      opacity: 0,
      display: 'none'
    })
    // 상단으로 스크롤 버튼 보이기!
    gsap.to(toTopEl, .2, {
      x: 0
    })

  // 페이지 스크롤 위치가 500px이 넘지 않으면.
  } else {
    // Badge 요소 보이기!
    gsap.to(badgeEl, .6, {
      opacity: 1,
      display: 'block'
    })
    // 상단으로 스크롤 버튼 숨기기!
    gsap.to(toTopEl, .2, {
      x: 100
    })
  }
}, 300))
// 상단으로 스크롤 버튼을 클릭하면,
toTopEl.addEventListener('click', function () {
  // 페이지 위치를 최상단으로 부드럽게(0.7초 동안) 이동.
  gsap.to(window, .7, {
    scrollTo: 0
  })
})
//공지사항. 수직으로 자동 넘김 
new Swiper('.notice-line .swiper-container', {
  direction: 'vertical',
  autoplay: true,
  loop: true
})

//메인화면 아랫부분 프로모션 3슬라이드
new Swiper('.promotion .swiper-container', {
  autoplay: { 
    delay: 5000 //5초 후 보여지게
  },
  loop: true,
  slidesPerView: 3, 
  spaceBetween: 10, 
  centeredSlides: true, 
//슬라이드 이전보기 다음보기
  pagination: { 
    el: '.promotion .swiper-pagination', //페이지 번호달기 
    clickable: true
  },
  navigation: {
    prevEl: '.promotion .swiper-prev',
    nextEl: '.promotion .swiper-next'
  }
})

//(선택자,클래스요소,기능) (어워즈부분)
new Swiper('.awards .swiper-container', {
  autoplay: true, 
  loop: true,
  spaceBetween: 30,
  slidesPerView: 5,
  navigation: {
    prevEl: '.awards .swiper-prev',
    nextEl: '.awards .swiper-next'
  }
})

//scroll magic 라이브러리 사용해서 페이지 요소에 토글 추가
const spyEls = document.querySelectorAll('section.scroll-spy')
spyEls.forEach(function (spyEl) {
  new ScrollMagic 
    .Scene({ 
      triggerElement: spyEl, //현재 보고있는 페이지 요소 실시간 확인
      triggerHook: .8  //80퍼까지 실행
    })
    .setClassToggle(spyEl, 'show')
    .addTo(new ScrollMagic.Controller())//
})

const thisYear = document.querySelector('.this-year')
thisYear.textContent = new Date().getFullYear()

//map