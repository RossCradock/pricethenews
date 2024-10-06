// only time range used to determine graph frequency

// TODO:
//- set up bokeh graph
    //- need to set graph size
    //- change margin/padding of interval picker
    //- need a way to resize based on screensize
    //- need to get rid of margin for mobile
    // colors and design of graph
//- js to highlight selected interval
//- set current date on actual date picker not just the text on the input
//- ticker symbol info.. maybe using yfinance info?
//- create a button to "Find Articles" 
//- use interval click to set start and end dates
//- interval picker resize to start and end of graph
//- create the yfinance data retreiver
//- the interval picker should show times only when changed but then stay on the one clicked upon mouseout event
//- set the full time frame on the datedisplay when not yet clicked
//- find articles needs to open FT tab when articles come back
//- response is expected to be in json so string responses don't work, need to change one side or the other
//- red set on clicked and return to it upon mouse out
//- img needs to be reset to width: 100% when mobile sized
//- update times button is overflowing
//- sort out nav bar 
//- artcle tabs to stretch to end of the page
//- ipad size not right
//- write meta data and change title
//- need to have default rerouted to non-local website address
//- navbar title is too right
//- & in the requests screw up guardian api calls
//- add in the github link
//- the scroll bar shouldn't be there for mobile
//- the time selector should be closed by default
//- find articles button fit in beside date (change the padding/margins to smaller on mobile)
// scroll to top of articles when new search complete or maybe highlight the element
//- favicon logo
//- stop sports articles 
//- interval picker stays on last touched interval instead of clicked one


function getE(id){
    return document.getElementById(id);
}

function getURLParams(){
    let ending = $('#date-picker').data('datepicker').getFormattedDate('yyyy-mm-dd');

    if(ending === ''){
        ending = moment().format('YYYY-MM-DD');
    }
    
    return '?range=' + RANGE_ARRAY[time_range_select.selectedIndex] +
        '&interval=' + INTERVAL_ARRAY[interval_select.selectedIndex] +
        '&ending=' + ending;
}

// NAV BAR DROPDOWNS \\
//forex
let forex_list_items = document.getElementsByClassName('forex-list-items');
for(let i = 0; i < forex_list_items.length; i++){
    forex_list_items[i].onclick = function() {
        location.pathname = 'f/' + forex_list_items[i].innerText.replace(' ⇄ ', '-');
    };
}


//stocks
let stocks_list_items = document.getElementsByClassName('stocks-list-items');
let stocks_url_holder = document.getElementsByClassName('stocks-url-holder');
for(let i = 0; i < stocks_list_items.length; i++){
    stocks_list_items[i].onclick = function() {
        location.pathname = 's/' + stocks_url_holder[i].innerText;
    };
}

// indices
var index_list_items = document.getElementsByClassName('index-list-items');
var index_symbol_items = document.getElementsByClassName('index-symbol-holder');
for(let i = 0; i < index_list_items.length; i++){
    index_list_items[i].onclick = function() {
        location.pathname = 'i/' + index_symbol_items[i].innerText;
    };
}

// DATE PICKER \\
$('.input-group input').datepicker({
    autoclose: true,
    weekStart: 1,
    startDate: '-15y',
    endDate: '0d',
    maxViewMode: 2,
    todayHighlight: true
}) // if nothing selected then set current date again
.on('hide', function(event){
    if(event.date === undefined){
       $('#date-picker').datepicker('setDate', moment().toDate());
       getE('date-picker').value = moment().format('DD/MM/YYYY');
    }
});

// set the calendar icon to open calendar like the input
getE('date-picker-icon').addEventListener('click', function(){
    getE('date-picker').focus();
}); 


// TIME PICKER \\
// elements
var time_range_select = getE('time-select-range');
var interval_select = getE('time-select-interval');
var update_button = getE('time-picker-update');

// select options
RANGE_ARRAY = ['3m', '6m', '1y', '2y', '3y', '5y'];
INTERVAL_ARRAY = ['1d', '2d', '3d', '1w', '2w', '4w'];

// set the selects & calendar to have the same options selected as the url 
let searchParams = new URLSearchParams(window.location.search);
time_range_select.selectedIndex = RANGE_ARRAY.indexOf(searchParams.get('range'));
interval_select.selectedIndex = INTERVAL_ARRAY.indexOf(searchParams.get('interval'));
calendar_date = moment(searchParams.get('ending'), 'YYYY-MM-DD');
$('#date-picker').datepicker('setDate', calendar_date.toDate());
getE('date-picker').value = calendar_date.format('DD/MM/YYYY');

update_button.addEventListener('click', function(){
    // go to new url
    location.href = getURLParams();
});

time_range_select.addEventListener('change', timeRangeSelectListener);

function timeRangeSelectListener(){
    switch(time_range_select.selectedIndex){
        case 0: // 3 months
            setDisabledOptions(true, 3);
            break;
        case 1: // 6 months
        case 2: // 1 year
            setDisabledOptions(false, 2)
            break;
        case 3: // 2 years
        case 4: // 3 years
            setDisabledOptions(false, 3);
            break;
        case 5: // 5 years
            setDisabledOptions(false, 4);
            break;
    }
}

// initialize upon page load
timeRangeSelectListener();

function setDisabledOptions(disableHigherOptions, index){
    // get the options as an array
    let options = interval_select.getElementsByTagName('option');

    // currently selected interval longer/shorter than allowed options? select the next closest option
    if((interval_select.selectedIndex > index && disableHigherOptions) ||
        (interval_select.selectedIndex < index && !disableHigherOptions)){
        interval_select.selectedIndex = index;
    }

    for (var i = 0; i < options.length; i++) {
        // set the disabled flag based on the options index
        options[i].disabled = (disableHigherOptions) ? (i > index) : (i < index);
    }
}

// set the collapsed time picker on mobile to open when going from < 768px to > 768px
$(window).resize(function(e) {
    let timePickerDisplay = window.getComputedStyle(getE('time-picker')).display === 'none';
    if(parseInt(window.innerWidth) > 770){
        if(timePickerDisplay){
        getE('time-picker-collapse-button').click();
    }
        getE('guardian-tab-button').style.width = 'none';
        getE('navbar-header').style.marginRight = '7em';
        getE('navbar-header').style.marginLeft = 0;
        document.getElementsByClassName('tabcontent')[0].style.maxHeight = 'calc(90vh - 501px)';
        document.getElementsByClassName('tabcontent')[1].style.maxHeight = 'calc(90vh - 501px)';
    }
    // mobile screen
    if(parseInt(window.innerWidth) < 770){
        getE('navbar-header').style.marginRight = 0;
        getE('navbar-header').style.marginLeft = 0;
        getE('articles-display').style.overflow = 'none';
        document.getElementsByClassName('tabcontent')[0].style.maxHeight = '100%';
        document.getElementsByClassName('tabcontent')[1].style.maxHeight = '100%';
    }
});
// when display is mobile
if(parseInt(window.innerWidth) < 770){
    getE('guardian-tab-button').click();
    getE('navbar-header').style.marginRight = 0;
    getE('navbar-header').style.marginLeft = 0;
    document.getElementsByClassName('tabcontent')[0].style.maxHeight = '100%';
    document.getElementsByClassName('tabcontent')[1].style.maxHeight = '100%';
    getE('time-picker').classList.remove('show');
}


// INTERVAL PICKER \\
const INTERVAL_HOVER_TIME = 100;
const INTERVAL_TIMES = [
    [1, 'day'],
    [2, 'day'],
    [3, 'day'],
    [1, 'week'],
    [2, 'week'],
    [4, 'week']
];

var interval_picker_buttons = document.getElementsByClassName('interval-picker-button');

var number_of_intervals = interval_picker_buttons.length 

// set interval picker left margin based on digits in price
y_axis_pixels = getE('y-axis-pixels-holder').innerHTML;
getE('interval-picker').style.paddingLeft = y_axis_pixels + 'px';


for(let i = 0; i < interval_picker_buttons.length; i++){
    var clicked = false;
    var clicked_interval;
    var interval_date_string;

    interval_picker_buttons[i].onclick = function() {
        // unset the red from the old interval that was picked
        if(clicked){
            interval_picker_buttons[clicked_interval].style.backgroundColor = 'unset';
        }

        clicked = true;
        clicked_interval = i;

        time_per_interval = INTERVAL_TIMES[interval_select.selectedIndex];
        interval_start = moment(calendar_date.utc()).subtract(time_per_interval[0] * (number_of_intervals - i) , time_per_interval[1]);
        interval_end = moment(interval_start.utc()).add(time_per_interval[0], time_per_interval[1]);

        clicked_interval_date_string = interval_start.format('DD-MM-YYYY') + ' until ' + 
            interval_end.format('DD-MM-YYYY')

        getE('date-display').innerHTML = clicked_interval_date_string;

        // show find articles button
        getE('find-articles-button').style.visibility = 'visible';
    };

    interval_picker_buttons[i].onmouseover = function(e) {
        timeout = setTimeout(function() {
            time_per_interval = INTERVAL_TIMES[interval_select.selectedIndex];
            interval_start = moment(calendar_date.utc()).subtract(time_per_interval[0] * (number_of_intervals - i) , time_per_interval[1]);
            interval_end = moment(interval_start.utc()).add(time_per_interval[0], time_per_interval[1]);

            interval_date_string = interval_start.format('DD-MM-YYYY') + ' until ' + 
            interval_end.format('DD-MM-YYYY')

            interval_picker_buttons[i].style.backgroundColor = 'red';
            getE('date-display').innerHTML = interval_date_string;
        }, INTERVAL_HOVER_TIME)
    };
    interval_picker_buttons[i].onmouseout = function(e) {
        if(timeout) {
            getE('date-display').innerHTML = (clicked) ? clicked_interval_date_string : 'Click on graph to select a time';
            interval_picker_buttons[i].style.backgroundColor = (clicked_interval == i) ? 'red' : 'unset';
            clearTimeout(timeout);
        }
    };
}

// ARTICLES \\
function tagsTextChange(search_tag){
    getE('search-tags-display').innerText = (search_tag) ? 
        'Search for term: "' + getE('tag-text-input').value + '"'
        : '';
}

function openTab(event, news_paper) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(news_paper).style.display = "block";
    event.currentTarget.className += " active";
}

function createHTMLForGuardianArticleCard(guardian_article){
    return  `                    <a target="_blank" rel="noopener noreferrer" href="https://www.theguardian.com/` + guardian_article.url_id + `">
                        <button class="article-card">
                            <div class="container-fluid">
                                <div class="clearfix">
                                    <div class="col-sm-9">
                                        <h4>` + guardian_article.title + `</h4>
                                    </div>
                                    <div class="col-sm-3">
                                        <p class="article-card-date">` + guardian_article.publish_date + `</p>
                                    </div>
                                </div>
                                <div class="clearfix">
                                    <h6>` + guardian_article.subtitle + `</h6>
                                </div>
                            </div>
                        </button>
                    `;
}

function addArticlesResponseToCard(response_data){
    try {
        response_data = JSON.parse(response_data);
    } catch(SyntaxError){
        // dont parse response data
    }
    if(response_data.toString().includes('Traceback (most recent call last):')) {
        const error_response_text = 'Something went wrong, please wait a moment and try again';
        getE('guardian').innerHTML = error_response_text;
        return;
    }

    let search_term = getE('tag-text-input').value;
    const no_results_text = (search_term) ? 
        'No results for that search term' :
        'No results for that time interval';
    if(response_data.data[0] == 'no results'){
        getE('guardian').innerHTML = no_results_text;
        return;
    }

    // good response
    let g_article_cards_html = '';
    for(let i = 0; i < response_data.data[0].length; i++){
        g_article_cards_html += createHTMLForGuardianArticleCard(response_data.data[0][i]);
    }
    getE('guardian').innerHTML = g_article_cards_html;
}

getE('find-articles-button').onclick = function() {
    let date_string = getE('date-display').innerText;
    let search_term = getE('tag-text-input').value;

    let request_data = {
        instrument: location.pathname.substring(1,2),
        name: location.pathname.substring(3).replace('%5E', '^'),
        start: date_string.substr(0,10),
        end: date_string.substr(date_string.length - 10, date_string.length),
        tag: search_term
    };

    request_data = JSON.stringify(request_data);
    $.post('/articles/', request_data, function(response_data, status){
        getE('guardian-tab-button').click();
        console.log(response_data);
        if(status === 'success'){
            addArticlesResponseToCard(response_data);
        } else{

        }
    })
};
