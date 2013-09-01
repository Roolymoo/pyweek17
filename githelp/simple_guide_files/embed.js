var DISQUS=function(e){var k=e.DISQUS||{};k.AssertionError=function(c){this.message=c};k.AssertionError.prototype.toString=function(){return"Assertion Error: "+(this.message||"[no message]")};k.assert=function(c,d,g){if(!c)if(g)e.console&&e.console.log("DISQUS assertion failed: "+d);else throw new k.AssertionError(d);};var d=[];k.define=function(c,l){typeof c==="function"&&(l=c,c="");for(var g=c.split("."),b=g.shift(),a=k,h=(l||function(){return{}}).call({overwrites:function(a){a.__overwrites__=!0;
return a}},e);b;)a=a[b]?a[b]:a[b]={},b=g.shift();for(var i in h)h.hasOwnProperty(i)&&(!h.__overwrites__&&a[i]!==null&&k.assert(!a.hasOwnProperty(i),"Unsafe attempt to redefine existing module: "+i,!0),a[i]=h[i],d.push(function(a,b){return function(){delete a[b]}}(a,i)));return a};k.use=function(c){return k.define(c)};k.cleanup=function(){for(var c=0;c<d.length;c++)d[c]()};return k}(window);
DISQUS.define(function(e,k){var d=e.DISQUS,c=e.document,l=c.getElementsByTagName("head")[0]||c.body,g={running:!1,timer:null,queue:[]};d.defer=function(b,a){function h(){var a=g.queue;if(a.length===0)g.running=!1,clearInterval(g.timer);for(var b=0,h;h=a[b];b++)h[0]()&&(a.splice(b--,1),h[1]())}g.queue.push([b,a]);h();if(!g.running)g.running=!0,g.timer=setInterval(h,100)};d.each=function(b,a){var h=b.length,i=Array.prototype.forEach;if(isNaN(h))for(var c in b)b.hasOwnProperty(c)&&a(b[c],c,b);else if(i)i.call(b,
a);else for(i=0;i<h;i++)a(b[i],i,b)};d.extend=function(b){d.each(Array.prototype.slice.call(arguments,1),function(a){for(var h in a)b[h]=a[h]});return b};d.serializeArgs=function(b){var a=[];d.each(b,function(b,i){b!==k&&a.push(i+(b!==null?"="+encodeURIComponent(b):""))});return a.join("&")};d.isString=function(b){return Object.prototype.toString.call(b)==="[object String]"};d.serialize=function(b,a,h){a&&(b+=~b.indexOf("?")?b.charAt(b.length-1)=="&"?"":"&":"?",b+=d.serializeArgs(a));if(h)return a=
{},a[(new Date).getTime()]=null,d.serialize(b,a);a=b.length;return b.charAt(a-1)=="&"?b.slice(0,a-1):b};d.require=function(b,a,h,i,f){function e(a){if(a.type=="load"||/^(complete|loaded)$/.test(a.target.readyState))i&&i(),j&&clearTimeout(j),d.bean.remove(a.target,k,e)}var g=c.createElement("script"),k=g.addEventListener?"load":"readystatechange",j=null;g.src=d.serialize(b,a,h);g.async=!0;g.charset="UTF-8";(i||f)&&d.bean.add(g,k,e);f&&(j=setTimeout(function(){f()},2E4));l.appendChild(g);return d};
d.requireStylesheet=function(b,a,h){var i=c.createElement("link");i.rel="stylesheet";i.type="text/css";i.href=d.serialize(b,a,h);l.appendChild(i);return d};d.requireSet=function(b,a,h){var i=b.length;d.each(b,function(b){d.require(b,{},a,function(){--i===0&&h()})})};d.injectCss=function(b){var a=c.createElement("style");a.setAttribute("type","text/css");b=b.replace(/\}/g,"}\n");e.location.href.match(/^https/)&&(b=b.replace(/http:\/\//g,"https://"));a.styleSheet?a.styleSheet.cssText=b:a.appendChild(c.createTextNode(b));
l.appendChild(a)};d.isString=function(b){return Object.prototype.toString.call(b)==="[object String]"}});
DISQUS.define("JSON",function(){function e(a){return a<10?"0"+a:a}function k(a){b.lastIndex=0;return b.test(a)?'"'+a.replace(b,function(a){var b=i[a];return typeof b==="string"?b:"\\u"+("0000"+a.charCodeAt(0).toString(16)).slice(-4)})+'"':'"'+a+'"'}function d(b,i){var o,c,t,g,e=a,s,n=i[b];n&&typeof n==="object"&&typeof n.toJSON==="function"&&!l&&(n=n.toJSON(b));typeof f==="function"&&(n=f.call(i,b,n));switch(typeof n){case "string":return k(n);case "number":return isFinite(n)?String(n):"null";case "boolean":case "null":return String(n);
case "object":if(!n)return"null";a+=h;s=[];if(Object.prototype.toString.apply(n)==="[object Array]"){g=n.length;for(o=0;o<g;o+=1)s[o]=d(o,n)||"null";t=s.length===0?"[]":a?"[\n"+a+s.join(",\n"+a)+"\n"+e+"]":"["+s.join(",")+"]";a=e;return t}if(f&&typeof f==="object"){g=f.length;for(o=0;o<g;o+=1)c=f[o],typeof c==="string"&&(t=d(c,n))&&s.push(k(c)+(a?": ":":")+t)}else for(c in n)Object.hasOwnProperty.call(n,c)&&(t=d(c,n))&&s.push(k(c)+(a?": ":":")+t);t=s.length===0?"{}":a?"{\n"+a+s.join(",\n"+a)+"\n"+
e+"}":"{"+s.join(",")+"}";a=e;return t}}var c={},l=!1;if(typeof Date.prototype.toJSON!=="function")Date.prototype.toJSON=function(){return isFinite(this.valueOf())?this.getUTCFullYear()+"-"+e(this.getUTCMonth()+1)+"-"+e(this.getUTCDate())+"T"+e(this.getUTCHours())+":"+e(this.getUTCMinutes())+":"+e(this.getUTCSeconds())+"Z":null},String.prototype.toJSON=Number.prototype.toJSON=Boolean.prototype.toJSON=function(){return this.valueOf()};var g=/[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
b=/[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,a,h,i={"\u0008":"\\b","\t":"\\t","\n":"\\n","\u000c":"\\f","\r":"\\r",'"':'\\"',"\\":"\\\\"},f;c.stringify=function(b,c,o){var i;h=a="";if(typeof o==="number")for(i=0;i<o;i+=1)h+=" ";else typeof o==="string"&&(h=o);if((f=c)&&typeof c!=="function"&&(typeof c!=="object"||typeof c.length!=="number"))throw Error("JSON.stringify");return d("",{"":b})};c.parse=function(a,b){function c(a,
i){var h,d,f=a[i];if(f&&typeof f==="object")for(h in f)Object.hasOwnProperty.call(f,h)&&(d=c(f,h),d!==void 0?f[h]=d:delete f[h]);return b.call(a,i,f)}var i,a=String(a);g.lastIndex=0;g.test(a)&&(a=a.replace(g,function(a){return"\\u"+("0000"+a.charCodeAt(0).toString(16)).slice(-4)}));if(/^[\],:{}\s]*$/.test(a.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g,"@").replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g,"]").replace(/(?:^|:|,)(?:\s*\[)+/g,"")))return i=eval("("+a+")"),
typeof b==="function"?c({"":i},""):i;throw new SyntaxError("JSON.parse");};var q={a:[1,2,3]},m,p;if(Object.toJSON&&Object.toJSON(q).replace(/\s/g,"")==='{"a":[1,2,3]}')m=Object.toJSON;typeof String.prototype.evalJSON==="function"&&(q='{"a":[1,2,3]}'.evalJSON(),q.a&&q.a.length===3&&q.a[2]===3&&(p=function(a){return a.evalJSON()}));(function(){var a=[1,2,3];typeof a.toJSON==="function"&&(a=a.toJSON(),l=!(a&&a.length===3&&a[2]===3))})();if(l||!m||!p)return{stringify:c.stringify,parse:c.parse};return{stringify:m,
parse:p}});
DISQUS.define(function(){function e(a){for(b=1;a=k.shift();)a()}var k=[],d,c=document,l=c.documentElement,g=l.doScroll,b=/^loade|c/.test(c.readyState),a;c.addEventListener&&c.addEventListener("DOMContentLoaded",d=function(){c.removeEventListener("DOMContentLoaded",d,!1);e()},!1);g&&c.attachEvent("onreadystatechange",d=function(){/^c/.test(c.readyState)&&(c.detachEvent("onreadystatechange",d),e())});a=g?function(c){self!=top?b?c():k.push(c):function(){try{l.doScroll("left")}catch(b){return setTimeout(function(){a(c)},50)}c()}()}:
function(a){b?a():k.push(a)};return{domready:a}});
DISQUS.define("Events",function(){var e=/\s+/,k=Object.keys||function(c){if(c!==Object(c))throw new TypeError("Invalid object");var d=[],g;for(g in c)Object.prototype.hasOwnProperty.call(c,g)&&(d[d.length]=g);return d},d={on:function(c,d,g){var b,a;if(!d)return this;c=c.split(e);for(b=this._callbacks||(this._callbacks={});a=c.shift();)a=b[a]||(b[a]=[]),a.push(d),a.push(g);return this},off:function(c,d,g){var b,a,h;if(!(a=this._callbacks))return this;if(!c&&!d&&!g)return delete this._callbacks,this;
for(c=c?c.split(e):k(a);b=c.shift();)if(!(h=a[b])||!d&&!g)delete a[b];else for(b=h.length-2;b>=0;b-=2)d&&h[b]!==d||g&&h[b+1]!==g||h.splice(b,2);return this},once:function(c,d,g){if(!d)return this;var b=this;return this.on(c,function h(){b.off(c,h);d.apply(this,arguments)},g)},trigger:function(c){var d,g,b,a,h,i,f;if(!(g=this._callbacks))return this;f=[];c=c.split(e);a=1;for(h=arguments.length;a<h;a++)f[a-1]=arguments[a];for(;d=c.shift();){if(i=g.all)i=i.slice();if(b=g[d])b=b.slice();if(b){a=0;for(h=
b.length;a<h;a+=2)b[a].apply(b[a+1]||this,f)}if(i){d=[d].concat(f);a=0;for(h=i.length;a<h;a+=2)i[a].apply(i[a+1]||this,d)}}return this}};d.bind=d.on;d.unbind=d.off;return d});
DISQUS.define(function(e){function k(){throw Error(Array.prototype.join.call(arguments," "));}function d(a,b,c){if(a.addEventListener)a.addEventListener(b,c,!1);else if(a.attachEvent)a.attachEvent("on"+b,c);else throw Error("No event support.");}function c(a,b,c){c||(c=0);var d,i,h,f,g=0,e=function(){g=new Date;h=null;f=a.apply(d,i)};return function(){var k=new Date,l=b-(k-g);d=this;i=arguments;l<=0?(clearTimeout(h),h=null,g=k,f=a.apply(d,i)):h||(h=setTimeout(e,l+c));return f}}var l=e.document,g=
DISQUS.use("JSON"),b={},a={},h=0;if(!(DISQUS.version&&DISQUS.version()==="2")){d(e,"message",function(b){var c,d;for(d in a)if(Object.prototype.hasOwnProperty.call(a,d)&&b.origin==a[d].origin){c=!0;break}if(c)switch(c=g.parse(b.data),(d=a[c.sender])||k("Message from our server but with invalid sender UID:",c.sender),c.scope){case "host":d.trigger(c.name,c.data);break;case "global":DISQUS.trigger(c.name,c.data);break;default:k("Message",c.scope,"not supported. Sender:",b.origin)}},!1);d(e,"hashchange",
function(){DISQUS.trigger("window.hashchange",{hash:e.location.hash})},!1);d(e,"resize",function(){DISQUS.trigger("window.resize")},!1);d(e,"scroll",c(function(){DISQUS.trigger("window.scroll")},250,50));d(l,"click",function(){DISQUS.trigger("window.click")});var i=function(){this.uid=h++;b[this.uid]=this};DISQUS.extend(i.prototype,DISQUS.Events);i.prototype.destroy=function(){delete b[this.uid]};DISQUS.extend(i,{listByKey:function(){var a={},c;for(c in b)Object.prototype.hasOwnProperty.call(b,c)&&
(a[c]=b[c]);return a},list:function(){var a=[],c;for(c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.push(b[c]);return a},get:function(a){if(Object.prototype.hasOwnProperty.call(b,a))return b[a];return null}});var f=function(b){b=b||{};this.state=f.INIT;this.uid=b.uid||h++;this.origin=b.origin;this.target=b.target;this.window=null;a[this.uid]=this;this.on("ready",function(){this.state=f.READY},this);this.on("die",function(){this.state=f.KILLED},this)};DISQUS.extend(f,{INIT:0,READY:1,KILLED:2});
DISQUS.extend(f.prototype,DISQUS.Events);f.prototype.sendMessage=function(a,b){var c=function(a,b,c){return function(){DISQUS.postMessage(c.window,a,b)}}(g.stringify({scope:"client",name:a,data:b}),this.origin,this);if(this.isReady())c();else this.on("ready",c)};f.prototype.hide=function(){};f.prototype.show=function(){};f.prototype.url=function(){return DISQUS.serialize(this.target,{disqus_version:"1370388847"})+"#"+this.uid};f.prototype.destroy=function(){this.state=f.KILLED;this.off()};f.prototype.isReady=
function(){return this.state===f.READY};f.prototype.isKilled=function(){return this.state===f.KILLED};var q=function(a){f.call(this,a);this.windowName=a.windowName};DISQUS.extend(q.prototype,f.prototype);q.prototype.load=function(){this.window=e.open("",this.windowName||"_blank");this.window.location=this.url()};q.prototype.isKilled=function(){return f.prototype.isKilled()||this.window.closed};var m=function(a){f.call(this,a);this.styles=a.styles||{};this.role=a.role||"application";this.container=
a.container;this.elem=null};DISQUS.extend(m.prototype,f.prototype);m.prototype.load=function(){var a=this.elem=l.createElement("iframe");a.setAttribute("id","dsq"+this.uid);a.setAttribute("data-disqus-uid",this.uid);a.setAttribute("allowTransparency","true");a.setAttribute("frameBorder","0");this.role&&a.setAttribute("role",this.role);DISQUS.extend(a.style,this.styles)};m.prototype.getOffset=function(){for(var a=this.elem,b=a,c=0,d=0;b;)c+=b.offsetLeft,d+=b.offsetTop,b=b.offsetParent;return{top:d,
left:c,height:a.offsetHeight,width:a.offsetWidth}};m.prototype.hide=function(){this.elem.style.display="none"};m.prototype.show=function(){this.elem.style.display=""};m.prototype.destroy=function(){f.prototype.destroy.call(this);this.elem&&this.elem.parentNode&&this.elem.parentNode.removeChild(this.elem)};var p=function(a){m.call(this,a);this.styles=DISQUS.extend({width:"100%",border:"none",overflow:"hidden",height:"0"},a.styles||{})};DISQUS.extend(p.prototype,m.prototype);p.prototype.load=function(a){var b=
this;m.prototype.load.call(b);var c=b.elem;c.setAttribute("width","100%");c.setAttribute("src",this.url());d(c,"load",function(){b.window=c.contentWindow;a&&a()});(DISQUS.isString(this.container)?l.getElementById(this.container)||l.body:this.container).appendChild(c)};var j=function(a){m.call(this,a);this.contents=a.contents;this.styles=DISQUS.extend({width:"100%",border:"none",overflow:"hidden"},a.styles||{})};DISQUS.extend(j.prototype,m.prototype);j.prototype.load=function(){m.prototype.load.call(this);
var a=this.elem;a.setAttribute("scrolling","no");(l.getElementById(this.container)||l.body).appendChild(a);this.window=a.contentWindow;try{this.window.document.open()}catch(b){a.src="javascript:var d=document.open();d.domain='"+l.domain+"';void(0);"}this.document=this.window.document;this.document.write(this.contents);this.document.close();if(a=this.document.body){var c=this.elem.style;c.height=c.minHeight=c.maxHeight=a.offsetHeight+"px"}};j.prototype.show=function(){this.elem.style.display="block"};
j.prototype.click=function(a){d(this.document.body,"click",function(b){a(b)})};var r=DISQUS.extend({},DISQUS.Events);return{log:function(a){var b=l.getElementById("messages");if(b){var c=l.createElement("p");c.innerHTML=a;b.appendChild(c)}},version:function(){return"2"},on:r.on,off:r.off,trigger:r.trigger,throttle:c,postMessage:function(a,b,c){a.postMessage(b,c)},WindowBase:f,Popup:q,Iframe:m,Channel:p,Sandbox:j,App:i}}});
DISQUS.define("next.host.utils",function(e){function k(b,a,c){var d,c=c||a;if(b===g)return"";e.getComputedStyle?d=g.defaultView.getComputedStyle(b,null).getPropertyValue(a):b.currentStyle&&(d=b.currentStyle[a]?b.currentStyle[a]:b.currentStyle[c]);return d=="transparent"||d===""||d=="rgba(0, 0, 0, 0)"?k(b.parentNode,a,c):d||null}function d(b){function a(a){a=Number(a).toString(16);return a.length==1?"0"+a:a}if(b.substr(0,1)==="#")return b;var c=/.*?rgb\((\d+),\s*(\d+),\s*(\d+)\)/.exec(b);if(!c||c.length!==
4)return"";var b=a(c[1]),d=a(c[2]),c=a(c[3]);return"#"+b+d+c}function c(b,a,c,d){DISQUS.isString(a)&&(a=g.createElement(a));var f=null;a.style.visibility="hidden";b.appendChild(a);f=k(a,c,d);b.removeChild(a);return f}function l(b){return b.toLowerCase().replace(/^\s+|\s+$/g,"").replace(/['"]/g,"")}var g=e.document;return{getContrastYIQ:function(b){b.match("^rgb")&&(b=d(b).substr(1));var a=parseInt(b.substr(0,2),16),c=parseInt(b.substr(2,2),16),b=parseInt(b.substr(4,2),16);return(a*299+c*587+b*114)/
1E3},colorToHex:d,getElementStyle:c,getAnchorColor:function(b){var a=g.createElement("a");a.href=+new Date;return c(b,a,"color")},normalizeFontValue:l,isSerif:function(b){for(var b=c(b,"span","font-family","fontFamily").split(","),a={courier:1,times:1,"times new roman":1,georgia:1,palatino:1,serif:1},d,i=0;i<b.length;i++)if(d=l(b[i]),a.hasOwnProperty(d))return!0;return!1},getBrowserSupport:function(b){if(b.postMessage){if(!b.JSON)return b.navigator.appName==="Microsoft Internet Explorer"?2:1}else return 1;
return 0}}});
DISQUS.define("next.host.switches",function(){function e(e){DISQUS.App.call(this);this.switches={};this.settings=e;this.url=e.useSSL?"https://securecdn.disqus.com/1370388847/build/next-switches/client_ssl.html":"http://mediacdn.disqus.com/1370388847/build/next-switches/client.html";this.origin=e.useSSL?"https://securecdn.disqus.com":"http://mediacdn.disqus.com"}e.prototype=DISQUS.extend({init:function(){this.frame=new DISQUS.Channel({target:this.url,origin:this.origin,container:this.settings.container,styles:{display:"none"}});
this.frame.load()},fetch:function(e){var d=this,e=e||{},c=e.success;delete e.success;this.frame.on("switches.received",function(e){d.switches=e;DISQUS.trigger("switches.changed",e);c&&c(e)});this.frame.sendMessage("fetch",e)},enabled:function(e){return this.switches[e]?this.switches[e]:!1}},DISQUS.App.prototype);return{Switches:function(k){return new e(k)}}});
DISQUS.define("next.host.profile",function(e){var k=function(d){DISQUS.App.call(this);d=d||{};d.fullscreen=d.fullscreen!==!1;this.frame=null;this.settings=d;d.useSSL?(this.url="https://disqus.com/embed/profile/",this.origin="https://disqus.com"):(this.url="http://disqus.com/embed/profile/",this.origin="http://disqus.com");this.url=DISQUS.serialize(this.url,{f:d.forum,language:d.language})};DISQUS.extend(k.prototype,DISQUS.App.prototype);k.prototype.init=function(){var d=this.settings,c={uid:this.uid,
target:this.url,origin:this.origin},l=d.fullscreen?{height:"100%",position:"fixed",top:0,left:0,zIndex:999999}:{height:"100%",padding:0},g=this.frame=d.windowName?new DISQUS.Popup(DISQUS.extend(c,{windowName:d.windowName})):new DISQUS.Channel(DISQUS.extend(c,{container:d.container||document.body,styles:l,role:"dialog"}));g.once("ready",function(){g.sendMessage("init",{referrer:e.location.href,fullscreen:d.fullscreen,switches:d.switches&&d.switches.switches});this.trigger("loading.init")},this);g.on("close",
function(){g.hide();e.focus()},this);g.on("renderProfile",function(b){this.trigger("renderProfile",b)},this);g.load();this.trigger("loading.start")};k.prototype.destroy=function(){this.frame&&this.frame.destroy()};k.prototype.show=function(d){DISQUS.isString(d)&&(d={username:d});var c=this.frame;if(!c.isReady())return void c.once("ready",function(){this.show(d)},this);c.sendMessage("showProfile",d);c.show()};return{Profile:function(d){return new k(d)}}});
DISQUS.define("next.host.backplane",function(){var e;try{localStorage.setItem("disqus.localStorageTest","disqus"),localStorage.removeItem("disqus.localStorageTest"),e=!0}catch(k){e=!1}var d=function(c){this.frame=c;this.credentials="unset";var d=this;typeof Backplane==="function"&&typeof Backplane.version==="string"&&typeof Backplane.subscribe==="function"&&e&&Backplane(function(){d.initialize()})};DISQUS.extend(d.prototype,{frameEvents:{invalidate:"clearCredentials"},initialize:function(){var c=
this;DISQUS.each(this.frameEvents,function(d,e){c.frame.on("backplane."+e,typeof d==="function"?d:c[d],c)});this.credentialsFromLocalStorage()&&this.frame.sendMessage("login",{backplane:this.credentials});this.subscribe()},subscribe:function(){var c=this;Backplane.subscribe(function(d){var e=c.handlers[d.type];e&&e.call(c,d)})},handlers:{"identity/login":function(c){var d=c.messageURL,c=c.channel;this.credentials!=="unset"&&this.credentials!==null&&this.credentials.channel===c&&this.credentials.messageUrl===
d||(this.setCredentials(c,d),this.frame.sendMessage("login",{backplane:this.getCredentials()}))}},credentialsFromLocalStorage:function(){var c=localStorage.getItem("disqus.backplane.channel"),d=localStorage.getItem("disqus.backplane.messageUrl");this.setCredentials(c,d,!0);return this.credentials},setCredentials:function(c,d,e){if(!c||!d)return void this.clearCredentials();e||(localStorage.setItem("disqus.backplane.channel",c),localStorage.setItem("disqus.backplane.messageUrl",d));this.credentials=
{channel:c,messageUrl:d}},getCredentials:function(){if(this.credentials!=="unset")return this.credentials;return this.credentialsFromLocalStorage()},clearCredentials:function(c){c=c||{};this.credentials=null;localStorage.removeItem("disqus.backplane.channel");localStorage.removeItem("disqus.backplane.messageUrl");if(c.redirectUrl)window.location=c.redirectUrl}});return{BackplaneIntegration:d}});
DISQUS.define("next.host.lounge",function(e,k){function d(a){for(var b=DISQUS.App.list(),c,d=0,e=b.length;d<e;d++)c=b[d],c instanceof g&&a(c)}var c=DISQUS.use("next.host.profile"),l=e.document,g=function(a){DISQUS.App.call(this);this.settings=a;this.indicators={north:null,south:null};this._boundGlobalEvents=[];this.frame=null;this.wasNearViewport=this.wasInViewport=!1};DISQUS.extend(g.prototype,DISQUS.App.prototype);g.prototype.init=function(){function a(a,b,d){j.on("affiliateLink",function(c){var e=
DISQUS.vglnk.$;if(!e)return void j.sendMessage("affiliateLink");e.request(a+"/click",{format:"jsonp",out:c.url,key:b,loc:j.target,subId:d},{fn:function(a){return function(b){var d={token:a};if(b)d.url=b;j.sendMessage("affiliateLink",d)}}(c.token),timeout:DISQUS.vglnk.opt("click_timeout")})})}function b(a,c){d._boundGlobalEvents.push(a);DISQUS.on(a,c,d)}var d=this,f=d.settings,g="http://disqus.com/embed/comments/",m="http://disqus.com";f.useSSL&&(g="https://disqus.com/embed/comments/",m="https://disqus.com");
var p={f:f.forum,t_i:f.identifier,t_u:f.url||e.location.href,t_s:f.slug,t_t:f.title||f.documentTitle,t_e:f.title,t_d:f.documentTitle,t_c:f.category,s_o:f.sortOrder,c:f.useConman||k};if(f.notSupported)p.n_s=f.notSupported;this.container=DISQUS.isString(f.container)?l.getElementById(f.container):f.container;var j=d.frame=new DISQUS.Channel({origin:m,target:DISQUS.serialize(g,p),container:f.container,uid:this.uid,role:"complementary"});f.notSupported||this.addLoadingAnim();j.on("ready",function(){var a=
{permalink:f.permalink,anchorColor:f.anchorColor,referrer:e.location.href,colorScheme:f.colorScheme,language:f.language,typeface:f.typeface,remoteAuthS3:f.remoteAuthS3,apiKey:f.apiKey,sso:f.sso,parentWindowHash:e.location.hash};if(e.navigator.userAgent.match(/(iPad|iPhone|iPod)/))a.width=j.elem.offsetWidth;j.sendMessage("init",a);d.trigger("loading.init")});j.on("resize",function(a){if(d.rendered)j.elem.style.height=a.height+"px",j.sendMessage("embed.resized"),d.scrollListener()});j.on("reload",function(){e.location.reload()});
j.on("reset",function(){DISQUS.reset({reload:!0})});j.on("session.identify",function(a){d.trigger("session.identify",a)});j.on("posts.paginate",function(){d.trigger("posts.paginate")});j.on("posts.create",function(a){d.trigger("posts.create",{id:a.id,text:a.raw_message})});j.on("scrollTo",function(a){var b=j.getOffset(),b=a.relative==="window"?a.top:b.top+a.top,c=d.getWindowYCoords();(a.force||!(b>c.pageYOffset&&b<c.pageYOffset+c.innerHeight))&&e.scrollTo(0,b)});j.on("realtime.init",function(a){var b=
["north","south"],c,e;e=j.getOffset().width+"px";for(var f={width:e,minWidth:e,maxWidth:e,position:"fixed"},h={north:{top:"0"},south:{bottom:"0"}},g=0;g<b.length;g++)e=b[g],c=new DISQUS.Sandbox({uid:"-indicator-"+e,container:d.settings.container,contents:a[e].contents,styles:DISQUS.extend(h[e],f),role:"alert"}),c.load(),c.hide(),function(a){c.click(function(){j.sendMessage("realtime.click",a)})}(e),d.indicators[e]=c});j.on("realtime.showNorth",function(a){var b=d.indicators.north;b.document.getElementById("message").innerHTML=
a;b.show()});j.on("realtime.hideNorth",function(){d.indicators.north.hide()});j.on("realtime.showSouth",function(a){var b=d.indicators.south;b.document.getElementById("message").innerHTML=a;b.show()});j.on("realtime.hideSouth",function(){d.indicators.south.hide()});j.on("mainViewRendered",function(a){d.rendered=!0;d.removeLoadingAnim();j.trigger("resize",a);j.sendMessage("embed.rendered");d.trigger("loading.done")});j.on("profile.show",function(a){if(!d.profile||d.profile.frame.isKilled())d.profile=
c.Profile({windowName:a.windowName,language:a.language,useSSL:f.useSSL,forum:f.forum,switches:f.switches}),d.profile.init();d.profile.show({id:a.userId})});j.once("loadLinkAffiliator",function(b){if(!e.vglnk_self&&!e.vglnk&&!function(){for(var a in e)if(a.indexOf("skimlinks")===0||a.indexOf("skimwords")===0)return!0;return!1}()){var c=b.apiUrl,d=b.key,f=String(b.id);if(!(b.clientUrl==null||c==null||d==null||b.id==null))DISQUS.define("vglnk",function(){return{api_url:c,key:d,sub_id:f}}),e.vglnk_self=
"DISQUS.vglnk",DISQUS.require(b.clientUrl),DISQUS.defer(function(){return DISQUS.vglnk.opt},function(){j.sendMessage("affiliationOptions",{timeout:DISQUS.vglnk.opt("click_timeout")})}),a(c,d,f)}});j.once("loadBackplane",function(){d.backplane=new DISQUS.next.host.backplane.BackplaneIntegration(j)});j.load(function(){f.notSupported?(j.elem.style.height="500px",j.elem.setAttribute("scrolling","yes"),j.elem.setAttribute("horizontalscrolling","no"),j.elem.setAttribute("verticalscrolling","yes"),j.show()):
(j.elem.setAttribute("scrolling","no"),j.elem.setAttribute("horizontalscrolling","no"),j.elem.setAttribute("verticalscrolling","no"))});b("window.hashchange",function(a){j.sendMessage("window.hashchange",a.hash)});b("window.resize",function(){j.sendMessage("window.resize")});b("window.scroll",d.scrollListener);b("window.click",function(){j.sendMessage("window.click")});b("switches.changed",function(a){j.sendMessage("switches.changed",a)});d.trigger("loading.start")};g.prototype.addLoadingAnim=function(){var a,
b,c,d=this.container,e=l.createElement("style");e.type="text/css";e.styleSheet?e.styleSheet.cssText=".disqus-loader{animation:disqus-embed-spinner .7s infinite linear;-webkit-animation:disqus-embed-spinner .7s infinite linear}@keyframes disqus-embed-spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@-webkit-keyframes disqus-embed-spinner{0%{-webkit-transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg)}}":e.appendChild(l.createTextNode(".disqus-loader{animation:disqus-embed-spinner .7s infinite linear;-webkit-animation:disqus-embed-spinner .7s infinite linear}@keyframes disqus-embed-spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@-webkit-keyframes disqus-embed-spinner{0%{-webkit-transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg)}}"));
a=l.createElement("div");b=l.createElement("div");c=l.createElement("div");b.appendChild(e);b.appendChild(c);a.appendChild(b);a.style.overflow="hidden";b.style.height=b.style.width="54px";b.style.margin="0 auto";b.style.overflow="hidden";c.style.height=c.style.width="29px";c.style.margin="11px 14px";c.className="disqus-loader";c.style.backgroundImage=b.style.backgroundImage="url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFMAAABmCAMAAACA210sAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5FVCB2My41LjEwMPRyoQAAAlhQTFRFMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtMzY63+TtWDj2BwAAAMh0Uk5TAAABAQICAwMEBAUFBgYHBwgICQkKCgsLDAwNDQ4ODw8QEBEREhITExQUFRUWFhcXGBgZGRoaGxscHB0dHh4fHyAgISEjIyQkJSUmJigoKSkqKisrLCwtLS4uLy8wMDExMjIzMzQ0NTU2Njc3ODg5OTo6Ozs8PD09Pj4/P0BAQUFCQkNDRERFRUZGR0dISElJS0tMTE1NTk5PT1BQUVFSUlNTVFRVVVZWV1dYWFlZWlpbW1xcXV1eXl9fYGBhYWJiY2NkZGVlZmaMInkiAAAFVklEQVRo3u2Yf0hbVxTHP/flmYYQxFoXghMJzkpXQmszCd0ma7eKKyKuSOlKGaV0RaRzsIHIGDK2MqSsXVvKcKWIG6V0ItI5Z1tXZBsiIkWciC0iYsMIIbisC1mWhpDG/RFjfpvr4O2vnH+Se+/J575z3z3n5n4F2Uy12aotpUY1HFp1OecXo+S00vo6q9kYXF2ZnfLG+0QWYH2jw5jcEZi6P50dW33qoBL//sl4TqbpyPHSzB97bo2GMjr1bcfUjcbcWXIwlZb24uxBenvH0sM+b0s0om2PAJPBC+hS3KxfvrUtx8IZD+z9LZDcUfL1zqTWj98DtLVP/JP2nIc74+vonplfWQ2EDcZya22deb3T1zOZtOq9saf0jMy6vSarywdU3tAvdIRTmGdOxz5Dd8cWkqeyNzXG1i16ZWijs+MEQPjaUCTh+EU9DFxNZna2AhAZvPUkPXDLqebY++3rj7/xfhXwfTyX5LX/EhA9tZxYz/bjACx0/vQ0YzEDk9O27QD2vx/Gej6oBiKdcylub24DsWN8g9ncAcDAp39mfUV/jJp3Aux//Big9CMF+Go8xcfveR14/k6cuatHB0Qvf5MrZ55NiH0Ajl/8wKEDgOezNOeVV8tAca8z9Zd3AFy4nTsLmRX7AP2Ld9bgxAvA4Ey6S9HLwNP11HrHCnBjmM2sbwTA1gJUAWQgmQKwxpiWkwAz19ncriwBtJugDMCZ4eAOAeYY84QeCPZE8zBDn0eA4qOgAvgzPQKASQEobQbo85DPlgcBjhkIA2SpNSVAQAFoMADeYfLbzSBQ8hpPACwZw2YV8CoATQCDIQmmbwTgMCsA9oxhO4BTASw1QGQMGRsBqDPNADSr6aPNADNKnD7rlWI6lwG1bioCVDSlDb5iB6ITClAL8AA5mwbY9eTXjaRPWs1ugEmvEt/AjySZjwCs9EcAQ3tK8bpUAkT7UYBKgGVJphOgAucAwI2kgfq+KoChJVRQTYA/IMl0AZTB9Vob9+cBSn1RxeJorAVg6RqoYIwngJRFQgYwQqSr19ILUH6LkCl+Iru6QglmEGkosdT0nXWsApzVo4+PLXZ5Y6NBWAdLmbrOxXcfoO6NxHk81BsmiVksjTSkRKV0bBAnvl3amDXiLwZTsV+OWQmQyA/9UF2V2Rj0OmcnvMmROPcAVXNbYLoS5W90NMNFAX4HsEnGvjt7NU5nLgA4JJn78yedEj9XasukkDXVQGQ2L9O9DKhNUswmgJlAXiZjAEdUCWRJC8Bd8jP9AOGIBPOkAfBNSjBbAW7LrOZRgIFQfubuXUBI4uwwdKuAL9/sCnAE4GeJPIrV9WuB/MziBgCJk7i9BWB+VKLKHDYAiwuo5RUW9/QmyJMAgXNRCWYrgP5qhVmBQHeus87Y1QhAjztvPDocbwNsLzcJQN+oPsy6p2wXXgLg4j0kmO9Zk9ui9tBfzrV0r/L3P9wOwPXvJHacKLudkT/O4fHkW4Jib2pYv3dclPlPhTh9Jl6nPW7vQcP698W5RddqMGQyVpbb7fHqEjg3KVUTxLA56Ha7XB63OwKV3ZuU0QfnPXLlUOxxpcTZ0laS4755dVz2yMq4Fxtbj2WppO6bd8P8Zyao9Q0OU8q9Z3p8Koq8CZF1h9lqaixlRn0w5HWtLCytsSVTc8y0rahIpxNFz3S6Ip1Y26J2ITTQLoQG2oXQQLsQGmgXQgPtQmigXQgNtAuhgXYhNNAuhAbahShoFwXtoqBdFLSLgnZR0C4K2kVBuyhoFwXtIofOIDTQLoQG2sVzGmgX72qgXfyggXaxVwPtQmigXYj/S7tQU7WLrQCBfwFnft8xK3413wAAAABJRU5ErkJggg==)";
c.style.backgroundRepeat=b.style.backgroundRepeat="no-repeat";c.style.backgroundPosition="-54px 0";if(this.settings.colorScheme==="dark")b.style.backgroundPosition="0 -51px",c.style.backgroundPosition="-54px -51px";d.appendChild(a);this.loadingElem=a;this.timeout=setTimeout(function(){if(a)(new Image).src=DISQUS.serialize("//juggler.services.disqus.com/stat.gif",{event:"slow_embed"}),b.insertAdjacentHTML("afterend",'<p align="center">Disqus seems to be taking longer than usual. <a href="#" onclick="DISQUS.reset({reload: true}); return false;">Reload</a>?</p>')},
1E4)};g.prototype.removeLoadingAnim=function(){var a=this.loadingElem,b=this.container;if(this.timeout)e.clearTimeout(this.timeout),this.timeout=null;a&&a.parentNode===b&&b.removeChild(a)};g.prototype.destroy=function(){var a=this.indicators;this.off();if(this._boundGlobalEvents.length)DISQUS.off(this._boundGlobalEvents.join(" "),null,this),this._boundGlobalEvents=null;this.frame&&this.frame.destroy();this.profile&&this.profile.destroy();if(a.north)a.north.destroy(),a.north=null;if(a.south)a.south.destroy(),
a.south=null;DISQUS.App.prototype.destroy.call(this)};g.prototype.getWindowYCoords=function(){if(typeof e.pageYOffset=="number")this.getWindowScroll=function(){return e.pageYOffset},this.getWindowHeight=function(){return e.innerHeight};else{var a=e.document,a=a.documentElement.clientHeight||a.documentElement.clientWidth?a.documentElement:a.body;this.getWindowScroll=function(){return a.scrollTop};this.getWindowHeight=function(){return a.clientHeight}}this.getWindowYCoords=function(){return{pageYOffset:this.getWindowScroll(),
innerHeight:this.getWindowHeight()}};return this.getWindowYCoords()};g.prototype.scrollListener=function(){var a=this.frame,b=a.getOffset(),c=b.top,d=c+b.height,e=this.getWindowYCoords(),g=e.pageYOffset,e=e.innerHeight,k=g+e,j=!1,l=!1;c<=k+e&&(l=(j=d>=g)&&c<=k);j&&(a.sendMessage("window.scroll",{frameOffset:b,pageOffset:g,height:e}),this.wasNearViewport||a.sendMessage("window.nearViewport"));this.wasNearViewport=j;if(l!==this.wasInViewport)a.sendMessage(l?"window.inViewport":"window.scrollOffViewport"),
this.wasInViewport=l};var b=function(a){return new g(a)};DISQUS.extend(b,{listByKey:function(){var a={};d(function(b){a[b.uid]=b});return a},list:function(){var a=[];d(function(b){a.push(b)});return a},get:function(a){a=DISQUS.App.get(a);return a instanceof g&&a}});return{Lounge:b}});
(function(e,k,d){function c(){function a(b){var b=b.getAttribute?b.getAttribute("src"):b.src,c=[/(https?:)\/\/(www\.)?disqus\.com\/forums\/([\w_\-]+)/i,/(https?:)\/\/(www\.)?([\w_\-]+)\.disqus\.com/i,/(https?:)\/\/(www\.)?dev\.disqus\.org\/forums\/([\w_\-]+)/i,/(https?:)\/\/(www\.)?([\w_\-]+)\.dev\.disqus\.org/i],d=c.length;if(!b||b.substring(b.length-8)!="embed.js")return null;for(var e=0;e<d;e++){var g=b.match(c[e]);if(g&&g.length&&g.length==4)return f=g[1]||null,g[3]}return null}for(var b=k.getElementsByTagName("script"),
c=b.length-1;c>=0;c--){var d=a(b[c]);if(d!==null)return d}return null}function l(){if(e.location.protocol==="https:")return!0;f===d&&c();return f==="https:"}function g(){for(var a=k.getElementsByTagName("h1"),b=k.title,c=b.length,e=b,g=0.6,f=0;f<a.length;f++)(function(a){var a=a.textContent||a.innerText,f;if(!(a===null||a===d)){f=0;for(var i=Array(b.length),h=0;h<=b.length;h++){i[h]=Array(a.length);for(var j=0;j<=a.length;j++)i[h][j]=0}for(h=0;h<b.length;h++)for(j=0;j<a.length;j++)b[h]==a[j]&&(i[h+
1][j+1]=i[h][j]+1,i[h+1][j+1]>f&&(f=i[h+1][j+1]));f/=c;f>g&&(g=f,e=a)}})(a[f]);return e}function b(){var b=k.getElementById(i);if(b){b.innerHTML="";var c=m.page;o=a.getBrowserSupport(e);b={container:i,forum:p,sortOrder:"default",permalink:q,useSSL:l(),language:m.language,typeface:a.isSerif(b)?"serif":"sans-serif",anchorColor:a.getAnchorColor(b),colorScheme:128<a.getContrastYIQ(a.getElementStyle(b,"span","color"))?"dark":"light",url:c.url||e.location.href.replace(/#.*$/,""),title:c.title,documentTitle:g(),
slug:c.slug,category:c.category_id,identifier:c.identifier,apiKey:c.api_key,remoteAuthS3:c.remote_auth_s3,sso:m.sso,useConman:e.disqus_demo,notSupported:o,switches:u};r=h.lounge.Lounge(b);var d={onReady:"loading.done",onNewComment:"posts.create",onPaginate:"posts.paginate",onIdentify:"session.identify"};DISQUS.each(m.callbacks,function(a,b){d[b]&&DISQUS.each(a,function(a){r.on(d[b],a)})});r.init()}else(b=e.console)&&typeof b.log==="function"&&b.log("DISQUS: Container (disqus_thread) element is missing.")}
var a=DISQUS.use("next.host.utils"),h=DISQUS.use("next.host"),i=e.disqus_container_id||"disqus_thread",f,q=function(){var a=e.location.hash;return(a=a&&a.match(/comment\-([0-9]+)/))&&a[1]}(),m={page:{url:d,title:d,slug:d,category_id:d,identifier:d,language:d,api_key:d,remote_auth_s3:d,author_s3:d,developer:d},strings:d,sso:{},callbacks:{preData:[],preInit:[],onInit:[],afterRender:[],onReady:[],onNewComment:[],preReset:[],onPaginate:[],onIdentify:[]}};DISQUS.each(["developer","shortname","identifier",
"url","title","category_id","language","slug"],function(a){var b=e["disqus_"+a];typeof b!=="undefined"&&(m.page[a]=b)});var p=e.disqus_shortname||c(),p=p.toLowerCase();if(typeof e.disqus_config==="function")try{e.disqus_config.call(m)}catch(j){}var r,o=0,u=h.switches.Switches({container:i,useSSL:l()});b();if(!o)u.init(),u.fetch({data:{forum:p}}),DISQUS.domready(function(){if(k.getElementsByClassName){var a=k.getElementsByClassName("dsq-brlink");a&&a.length&&a[0].parentNode.removeChild(a[0])}}),DISQUS.request=
{get:function(a,b,c){DISQUS.require(a,b,c)}},DISQUS.reset=function(a){a=a||{};if(typeof a.config==="function")try{a.config.call(m)}catch(c){}r&&(r.destroy(),r=null);a.reload&&(b(),DISQUS.trigger("switches.changed",u.switches))}})(this,this.document);