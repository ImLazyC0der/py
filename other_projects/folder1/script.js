import anime from "https://cdn.skypack.dev/animejs@3.2.1";

anime({
  targets: '.birthday-cake svg path',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 5000,
  delay: function (el, i) {return i * 250;},
  direction: 'forwards' });