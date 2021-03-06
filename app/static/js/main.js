// Get default user data

//TODO 
// Make sure all colors are used via variable names

// Colors
var bg_color = getComputedStyle(document.documentElement)
.getPropertyValue('--bg-color');

var bg_color_lighter = getComputedStyle(document.documentElement)
.getPropertyValue('--bg-color-lighter');

var main_color = getComputedStyle(document.documentElement)
.getPropertyValue('--main-color');

var caret_color = getComputedStyle(document.documentElement)
.getPropertyValue('--caret-color');

var sub_color = getComputedStyle(document.documentElement)
.getPropertyValue('--sub-color');

var text_color_important = getComputedStyle(document.documentElement)
.getPropertyValue('--text-color-important');

var text_color = getComputedStyle(document.documentElement)
.getPropertyValue('--text-color');

var error_color = getComputedStyle(document.documentElement)
.getPropertyValue('--error-color');

var error_extra_color = getComputedStyle(document.documentElement)
.getPropertyValue('--error-extra-color');


var users_data = []
const getDefaultData = async () => {
    try {
        let prod = 'http://www.weuphere.com/api/users';
        let dev = 'http://127.0.0.1:5000/api/users';
    
        if (window.location.hostname == "127.0.0.1") {
            var response = await fetch(dev, {
                method: 'POST'
            });
        } else if (window.location.hostname == "www.weuphere.com") {
            var response = await fetch(prod, {
                method: 'POST'
            });
        } else {
           var response = 'none';
        }

        const data = await response.json()
        // Call function to render users inside
        for (let i = 0; i < data.length; i++) {
            users_data.push(data[i]);
        }
        renderUsers(data, 50);
    } catch (error) {
        console.log(error)
    }
}

const retrieveDefaultData = async () => {
    await getDefaultData();
}

retrieveDefaultData();

var usersToDisplay = 50;

// Display users
function renderUsers (users, amount) {
    // parent div
    let content = document.getElementById('middle-content');
    if (content) {
        for (let i = 0; i < amount; i++) {
            // Create container div
            if (users[i]) {
                let user = document.createElement('div');
                user.className = 'user';
                user.id = 'user-' + users[i].id;
                content.appendChild(user)
    
                // Create container div
                let user_profile_box = document.createElement('div');
                user_profile_box.className = 'user_profile_box';
                user_profile_box.id = 'user_profile_box-' + users[i].id;
                user_profile_box.classList.add('animate__animated', 'animate__fadeInUp');
                user_profile_box.addEventListener('click', displayUserPage.bind(event, users[i].id), false)
                user.appendChild(user_profile_box);
    
                // If user is online create div (circle blue color)
                if (users[i].online){
                    let online_icon = document.createElement('div');
                    online_icon.className = 'online-icon';
                    user_profile_box.appendChild(online_icon);
                }
                // Create profile img from link
                let user_img = document.createElement('img');
                user_img.src = users[i].profile_image; 
                user_img.id = 'user-img-' + users[i].id;
                user_profile_box.appendChild(user_img)
    
                // Userpage div container
                let userpage = document.createElement('div');
                userpage.className = 'userpage';
                userpage.id = 'userpage-' + users[i].id;
                userpage.classList.add('animate__animated', 'animate__backInUp');
                user.appendChild(userpage);
    
                // Userpage content container
                let userpage_content = document.createElement('div');
                userpage_content.className = 'userpage-content';
                userpage.appendChild(userpage_content);
    
                // Main top level content
                let main_content = document.createElement('div');
                main_content.className = 'main-content';
                userpage_content.appendChild(main_content);
    
                // arrow box
                let arrow_box_left = document.createElement('div');
                arrow_box_left.className = 'arrow-box';
                arrow_box_left.id = 'arrow-box-left';
                main_content.appendChild(arrow_box_left);
                
                let arrow_img = document.createElement('img');
                arrow_img.className = 'left-arrow-img';
                arrow_img.src = window.location.href + 'static/img/button-icons/left-arrow.png';
                arrow_img.addEventListener('click', lastUserpage, false);
                arrow_box_left.appendChild(arrow_img);
    
                // Middle content
                let middle_content = document.createElement('div');
                middle_content.className = 'userpage-middle-content';
                main_content.appendChild(middle_content);
    
                // Profile pic box
                let profile_pic_box = document.createElement('div');
                profile_pic_box.className = 'profile_pic_box';
                middle_content.appendChild(profile_pic_box);
                let user_profile_box_userpage = document.createElement('div');
                user_profile_box_userpage.className = 'user_profile_box-userpage';
                profile_pic_box.appendChild(user_profile_box_userpage);
                let userpage_image = document.createElement('img');
                userpage_image.src = users[i].profile_image;
                user_profile_box_userpage.appendChild(userpage_image);
    
                // Basic user info
                let user_basic_info = document.createElement('div');
                user_basic_info.className = 'user_basic_info';
                middle_content.appendChild(user_basic_info);
    
                let username_box = document.createElement('div');
                username_box.className = 'username-box';
                user_basic_info.appendChild(username_box);
    
                let username_span = document.createElement('span');
                username_span.innerHTML = users[i].username;
                username_span.className = 'username';
                username_box.appendChild(username_span);
    
                let location_box = document.createElement('div');
                location_box.className = 'location-box';
                user_basic_info.appendChild(location_box); 
    
                let location_image = document.createElement('img');
                location_image.src = window.location.href + 'static/img/button-icons/location.png';
                location_box.appendChild(location_image);
    
                let location_span = document.createElement('span');
                location_span.innerHTML = users[i].location;
                location_box.appendChild(location_span);
    
                let age_box = document.createElement('div');
                age_box.className = 'username-age';
                user_basic_info.appendChild(age_box);
    
                let age_image = document.createElement('img');
                age_image.src = window.location.href + 'static/img/button-icons/user.png';
                age_box.appendChild(age_image);
    
                let user_age = document.createElement('span');
                user_age.innerHTML = users[i].age;
                age_box.appendChild(user_age);
    
                // Right side content
                let right_side_content = document.createElement('div');
                right_side_content.className = 'right-side-content';
                main_content.appendChild(right_side_content);
    
                let close_box = document.createElement('div');
                close_box.className = 'close-box';
                close_box.addEventListener('click', hideUserPageOnX, false)
                right_side_content.appendChild(close_box);
    
                let close_image = document.createElement('img');
                close_image.src = window.location.href + 'static/img/button-icons/close.png';
                close_box.appendChild(close_image);
    
                let arrow_box = document.createElement('div');
                arrow_box.className = 'arrow-box';
                arrow_box.id = 'arrow-box-right';
                right_side_content.appendChild(arrow_box);
    
                let arrow_image = document.createElement('img');
                arrow_image.className = 'right-arrow-img';
                arrow_image.src = window.location.href + 'static/img/button-icons/right-arrow.png';
                arrow_image.addEventListener('click', nextUserpage, false);
                arrow_box.appendChild(arrow_image);
    
                // Social media container
                let social_media_content = document.createElement('div');
                social_media_content.className = 'social-media-content';
                userpage_content.appendChild(social_media_content);
    
                let element_a = document.createElement('a');
                element_a.href = users[i].facebook;
                element_a.target = '_blank';
                social_media_content.appendChild(element_a);
    
                let facebook_image = document.createElement('img');
                facebook_image.src = window.location.href + 'static/img/social-media-icons/facebook-img.png';
                element_a.appendChild(facebook_image);
    
                let element_a_2 = document.createElement('a');
                element_a_2.href = users[i].twitter;
                element_a_2.target = '_blank';
                social_media_content.appendChild(element_a_2);
    
                let twitter_image = document.createElement('img');
                twitter_image.src = window.location.href + 'static/img/social-media-icons/twitter-img.png';
                element_a_2.appendChild(twitter_image);
    
                let element_a_3 = document.createElement('a');
                element_a_3.href = users[i].youtube;
                element_a_3.target = '_blank';
                social_media_content.appendChild(element_a_3);
    
                let youtube_image = document.createElement('img');
                youtube_image.src = window.location.href + 'static/img/social-media-icons/youtube-img.png';
                element_a_3.appendChild(youtube_image);
    
                let element_a_4 = document.createElement('a');
                element_a_4.href = users[i].spotify;
                element_a_4.target = '_blank';
                social_media_content.appendChild(element_a_4);
    
                let spotify_image = document.createElement('img');
                spotify_image.src = window.location.href + 'static/img/social-media-icons/spotify-img.png';
                element_a_4.appendChild(spotify_image);
            }
        }
        if (users.length != amount) {
            if ((content.children.length) != users_data.length) {
                let view_more_box = document.createElement('div');
                view_more_box.id = 'view-more-users-box';
                content.appendChild(view_more_box);
    
                let view_more = document.createElement('div');
                view_more.id = 'view-more';
                view_more_box.appendChild(view_more);
    
                let span = document.createElement('span');
                span.innerHTML = 'Load more'
                view_more.appendChild(span);
                view_more.classList.add('animate__animated', 'animate__fadeInUp');
    
                view_more.addEventListener('click', e => {
                    usersToDisplay += 50;
                    state.current = ''
                    state.displayed = false
                    clearUsers();
                    renderUsers(users_data, usersToDisplay);
                })
            }
        }
    }
}


// Variable holding the current state of some 'user-page'
var state = {
    'displayed': false,
    'current' : ''    // 'user-5', 'user-76'
}


var displayUserPage = function (user_id) {
    let userpage = 'userpage-' + user_id;
    let userpage_element = document.getElementById(userpage);

    let user_img = document.getElementById('user-img-' + user_id);
    user_img.style.borderRadius = '40px';
    
    // close window if user clicks on him self again
    if (state.current == userpage && state.displayed == true) {
        userpage_element.classList.toggle('display-block');
        user_img.style.borderRadius = '8px';
        state.displayed = false;
        state.current = '';
        // if window closed open when clicked on user
    } else if (state.current == '' && state.displayed == false) {
        userpage_element.classList.toggle('display-block');
        state.displayed = true;
        state.current = userpage;
        // if user clicks on another user when window opened 
        // close and open new
    } else if (state.current != '' && state.displayed == true) {
        let current_user_img = document.getElementById('user-img-' + state.current.split('-')[1]);
        current_user_img.style.borderRadius = '8px';
        page_to_close = document.getElementById(state.current);
        page_to_close.classList.toggle('display-block');
        userpage_element.classList.toggle('display-block');
        state.current = userpage;
    }
}


var lastUserpage = function () {
    // TODO
    // get array of userpages
    let userpages = document.getElementsByClassName('userpage');
    
    // find location of current open userpage in that array
    for (let i = 0; i < userpages.length; i++) {
        if (userpages[i].id == state.current) {
            // hide it and show a new userpage of index -1 in that array
            if (i != 0) {
                let current_userpage = document.getElementById(state.current);
                let current_user_img = document.getElementById('user-img-' + state.current.split('-')[1]);
                current_user_img.style.borderRadius = '8px';
                current_userpage.classList.remove('animate__fadeInLeft', 'animate__fadeInRight')
                current_userpage.classList.toggle('display-block');

                let new_userpage = document.getElementById(userpages[i - 1].id);
                new_userpage.classList.add('animate__animated', 'animate__fadeInLeft');
                new_userpage.classList.toggle('display-block');
                
                state.current = userpages[i - 1].id;

                let new_user_img = document.getElementById('user-img-' + state.current.split('-')[1]);
                new_user_img.style.borderRadius = '40px';
                new_user_img.scrollIntoView({behavior: 'smooth', block: "center"});
                break;
            }
        } 
    }
}

var nextUserpage = function () {
    let userpages = document.getElementsByClassName('userpage');
    for (let i = 0; i < userpages.length - 1; i++) {
        if (userpages[i].id == state.current) {
            if (i < userpages.length) {
                let current_userpage = document.getElementById(state.current);
                let current_user_img = document.getElementById('user-img-' + state.current.split('-')[1]);
                current_user_img.style.borderRadius = '8px';
                current_userpage.classList.remove('animate__fadeInLeft', 'animate__fadeInRight');
                current_userpage.classList.toggle('display-block');
                
                let new_userpage = document.getElementById(userpages[i + 1].id);
                new_userpage.classList.add('animate__animated', 'animate__fadeInRight');
                new_userpage.classList.toggle('display-block');
                
                state.current = userpages[i + 1].id;

                let new_user_img = document.getElementById('user-img-' + state.current.split('-')[1]);
                new_user_img.scrollIntoView({behavior: 'smooth', block: "center"});
                new_user_img.style.borderRadius = '40px';
                break;
            }
        }
    }
}


document.addEventListener('keydown', function(event) {
    if (event.keyCode == 37 && state.displayed) {
        lastUserpage();
    }
    else if (event.keyCode == 39 && state.displayed) {
        nextUserpage();
    }
})


var hideUserPageOnX = function () {
    let userpage_element = document.getElementById(state.current);
    let user_img = document.getElementById('user-img-' + state.current.split('-')[1]);
    user_img.style.borderRadius = '8px';
    userpage_element.classList.toggle('display-block');
    state.displayed = false;
    state.current = '';
}

// Arrow input for chaning userpages


function getFilteredUsers(search_string) {
    let content = document.getElementById('middle-content');
    let searchbar = document.getElementById('searchbar');
    state.current = '';
    state.displayed = false;
    if (search_string.length == 0 && !content.firstChild) {
        searchbar.style.color = '#212135';
        renderUsers(users_data, usersToDisplay);
    } else if (search_string.length == 0 && content.children[0].id == 'no-result-box') {
        clearUsers();
        renderUsers(users_data, usersToDisplay);
    } else if (search_string.length == 0) {
        clearUsers();
        renderUsers(users_data, usersToDisplay);
    }
    else if (search_string.length != 0) {
        const filteredUsers = users_data.filter(user => {
            return (
                user.username.toLowerCase().includes(search_string.toLowerCase()) || 
                user.paramaters.toLowerCase().includes(search_string.toLowerCase()) ||
                user.location.toLowerCase().includes(search_string.toLowerCase())
                );
            });
        searchbar.style.color = '#212135';
        clearUsers();
        renderUsers(filteredUsers, filteredUsers.length)
    } 
    if (search_string.length != 0 && !content.firstChild) {
        
        // Change input color when nothing shows up
        searchbar.style.color = error_color;

        no_result_box = document.createElement('div');
        no_result_box.id = 'no-result-box';
        no_result_box.className = 'no-result-box';
        no_result_box.classList.add('animate__animated', 'animate__fadeIn');
        content.appendChild(no_result_box);

        p = document.createElement('p');
        p.innerHTML = 'No results found.'
        no_result_box.appendChild(p);
    }
}


function clearUsers() {
    let content = document.getElementById('middle-content');
    while (content.firstChild) {
        content.firstChild.remove()
    }
} 


window.onload = function() {
    // Listen for search input

    const searchbar = document.getElementById('searchbar');
    
    if (searchbar) {
        searchbar.addEventListener('keyup', e => {
            const searchString = e.target.value;
            getFilteredUsers(searchString);
        });
    }

    navbar_clickable_profile = document.getElementById('navbar-clickable-profile');
    if (navbar_clickable_profile) {
        navbar_clickable_profile.addEventListener('click', () => {
            navbar_profile_items = document.getElementById('navbar-profile-items');
            navbar_profile_items.classList.toggle('display-grid');
        }); 
    }
}