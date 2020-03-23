import Axios from 'axios';

const clientId = 'UYpBkKY6vYW72ayc7ovAZ5xvUapQ3a8TucsGI2jS';
const clientSecret = 'REvBZR4e1yVflIrF1FAWcLVl08ZtewuxinaQsSNt6XKpxar6v17LvjkrCkKVDqHQUTDCcLfuZfm1V7JQ0C9qdKnYQpbjjjMrYMt76kdzTtE3xGv4ZaxdX9TnLsTeadZu';

let _accessToken;

export function getAccessToken() {
  return new Promise((resolve) => {
    if (_accessToken) { // if accesstoken is already present, resolve promise immediately
      resolve(_accessToken);
    } else { // else set access token with client credentials
      const data = {
        grant_type: 'client_credentials',
        client_id: clientId,
        client_secret: clientSecret,
        scope: 'read'
      }
      Axios.post('/oauth/token/', data).then((response) => {
        _accessToken = response.data.access_token;
        resolve(_accessToken);
      }); // provide the credentials to Django oauth default API, which will return a unique token that we can then use to resolve our promise
    }
  });
}

export async function getConfig() {
  const accessToken = await getAccessToken(); // asynchronously gets the applications oAuth access token
  const config = {
    headers: {
      Authorization: `Bearer ${accessToken}`
    }
  }; // sets up header with access token
  return new Promise((resolve) => {
    resolve(config);
  }); // resolve promise
}

export default {
  async retrieveWishlist() {
    const config = await getConfig(); // configs for HTTP request methods
    return new Promise((resolve) => {
      Axios.get('/api/v1/wishlist/', config).then((response) => {
        resolve(response.data);
      }); // get wishlist 
    });
  },

  async wishlistAdd(id) {
    const config = await getConfig();
    const data = { id };
    return Axios.post('/api/v1/wishlist/', data, config);
  },

  // Delete item from Wishlist
  async wishlistDelete(itemId) {
    const config = await getConfig();
    return Axios.delete(`/api/v1/wishlist/${itemId}/`, config);
  },

  async wishlistCartStatus(id, added_to_cart) {
    const config = await getConfig();
    const data = { id, added_to_cart };
    return Axios.patch(`/api/v1/wishlist/${id}/`, data, config);
  },

  async retrieveDetails(id) {
    const config = await getConfig();
    return new Promise((resolve) => {
      Axios.get(`/api/v1/public/packages/${id}/`, config).then((response) => {
        resolve(response.data);
      });
    });
  },
  
  // Retrieve List of packages by calling Django REST API
  async retrieveList(pageIndex, queryParams) {
    const config = await getConfig(); // To get React Config app token
    config['params'] = queryParams; // params to send to API
    config['params']['page'] = pageIndex;
    return new Promise((resolve) => {
      Axios.get('/api/v1/public/packages/', config).then((response) => {
        resolve(response.data);
      });
    });
  },

  async createBooking(data) {
    const config = await getConfig();
    return new Promise((resolve) => {
      Axios.post('/api/v1/bookings/', data, config).then((response) => {
        resolve(response.data)
      });
    })
  }
}
