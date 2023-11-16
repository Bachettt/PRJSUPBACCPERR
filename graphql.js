/* eslint-disable max-len */
import { createClient, defaultExchanges } from '@urql/core';
 
/**
 * For the purpose of this example we use urgl - lightweights GraphQL client.
 * To establish a connection with Chargetrip GraphQL API you need to have an API key.
 * The key in this example is a public one and gives an access only to a part of our extensive database.
 * You need a registered `x-client-id` to access the full database.
 * Read more about an authorisation in our documentation (https://docs.chargetrip.com/#authorisation).
 */
const headers = {
  'x-client-id': '65265ed612e5356e23ce69ad',
  'x-app-id': '65265ed612e5356e23ce69af',
};
 
const client = createClient({
  url: 'https://api.chargetrip.io/graphql',
  fetchOptions: {
    method: 'POST',
    headers,
  },
  exchanges: [...defaultExchanges],
});
 
/**
 * The function that handles all our GraphQL networking alongside it's parameters.
 * @param { Object } - Object that manages the page, size and search to be send towards our request
 * @param { number } page - Number of the page we are on
 * @param { number } size - Number of vehicles that we should fetch in one request
 * @param { string } search - The keywords that we should filter our vehicle list on
 */

const vehicleListQuery = qql`
query vehicleList($page: Int, $size: Int, $search: String) {
  vehicleList(
    page: $page, 
    size: $size, 
    search: $search, 
  ) {
    id
    naming {
      make
      model
      chargetrip_version
    }
    media {
      image {
        thumbnail_url
      }
    }
  }
}
`;

client.request(vehicleListQuery, variables)
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });

