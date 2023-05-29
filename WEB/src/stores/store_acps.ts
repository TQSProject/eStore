import { writable, derived } from 'svelte/store';

export interface ACPType {
  id: number;
  name: string;
  city: string;
  // Add any additional properties here
}

/** Store for your data. 
This assumes the data you're pulling back will be an array.
If it's going to be an object, default this to an empty object.
**/
export const acps = writable<ACPType[]>([]);

/** Data transformation.
For our use case, we only care about the drink names, not the other information.
Here, we'll create a derived store to hold the drink names.
**/
export const acpIDs = derived(acps, ($acps) => {
  if ($acps){
    return $acps.map(acp => `${acp.name}, ${acp.city}`);
  }
  return [];
});