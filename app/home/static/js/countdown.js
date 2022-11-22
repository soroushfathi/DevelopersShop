

/* Promotion Countdown */
jQuery(document).ready(function($) {
  $.fn.ENGO_CountDown = function( options ) {
    return this.each(function() {
      // get instance of the ENGO_CountDown.
      new  $.ENGO_CountDown( this, options );
    });
  }
  $.ENGO_CountDown = function( obj, options ){
    var ddiff, gsecs;
    this.options = $.extend({
      autoStart           : true,
      LeadingZero:true,
      DisplayFormat:"<div><span>%%D%%</span> Days</div><div><span>%%H%%</span> Hours</div><div><span>%%M%%</span> Mins</div><div><span>%%S%%</span> Secs</div>",
      FinishMessage:"Expired",
      CountActive:true,
      TargetDate:null
    }, options || {} );
    if( this.options.TargetDate == null || this.options.TargetDate == '' ){
      return ;
    }
    this.timer  = null;
    this.element = obj;
    this.CountStepper = -1;
    this.CountStepper = Math.ceil(this.CountStepper);
    this.SetTimeOutPeriod = (Math.abs(this.CountStepper)-1)*1000 + 990;
    var dthen = new Date(this.options.TargetDate);
    var dnow = new Date();
    if( this.CountStepper > 0 ) {
      ddiff = new Date(dnow-dthen);
    }
    else {
      ddiff = new Date(dthen-dnow);
    }
    gsecs = Math.floor(ddiff.valueOf()/1000);
    this.CountBack(gsecs, this);
  };
  $.ENGO_CountDown.fn =  $.ENGO_CountDown.prototype;
  $.ENGO_CountDown.fn.extend =  $.ENGO_CountDown.extend = $.extend;
  $.ENGO_CountDown.fn.extend({
    calculateDate:function( secs, num1, num2 ){
      var s = ((Math.floor(secs/num1))%num2).toString();
      if ( this.options.LeadingZero && s.length < 2) {
        s = "0" + s;
      }
      return "<b>" + s + "</b>";
    },
    CountBack:function( secs, self ){
      var DisplayStr;
      if (secs < 0) {
        self.element.innerHTML = '<div class="labelexpired"> '+self.options.FinishMessage+"</div>";
        return;
      }
      clearInterval(self.timer);
      DisplayStr = self.options.DisplayFormat.replace(/%%D%%/g, self.calculateDate( secs,86400,100000) );
      DisplayStr = DisplayStr.replace(/%%H%%/g, self.calculateDate(secs,3600,24));
      DisplayStr = DisplayStr.replace(/%%M%%/g, self.calculateDate(secs,60,60));
      DisplayStr = DisplayStr.replace(/%%S%%/g, self.calculateDate(secs,1,60));
      self.element.innerHTML = DisplayStr;
      if (self.options.CountActive) {
        self.timer = null;
        self.timer =  setTimeout( function(){
          self.CountBack((secs+self.CountStepper),self);
        },( self.SetTimeOutPeriod ) );
      }
    }

  });

  function init_countdown() {
    /** Countdown **/
    $('[data-countdown="countdown"]').each(function(index, el) {
      var $this = $(this);
      var $date = $this.data('date').split("-");
      $this.ENGO_CountDown({
        TargetDate:$date[0]+"/"+$date[1]+"/"+$date[2]+" "+$date[3]+":"+$date[4]+":"+$date[5],
        // DisplayFormat:"<li><span>%%D%% :</span></li><li><span>%%H%% :</span></li><li><span>%%M%% :</span></li><li><span>%%S%%</span></li>",
        DisplayFormat:"<ul><li><p>%%D%% </p><span>روز</span></li><li><p>%%H%%</p><span>ساعت</span></li><li><p>%%M%% </p><span>دقیقه</span></li><li><p>%%S%%</p><span>ثانیه</span></li></ul>",
        FinishMessage: "Expired"
      });
    });

  }
  init_countdown();
});



