<!-- <script>
  import { onMount } from 'svelte';
  import { Grid } from "gridjs";
  import "gridjs/dist/theme/mermaid.css";
  import { RowSelection } from "gridjs/plugins/selection";
  import { faker } from '@faker-js/faker';

let gridContainer2;

  const grid = new Grid({
  columns: [
      {
        id: 'selectRow',
        name: 'Select',
        // select all rows by default!
        data: () => true, 
        plugin: {
          component: RowSelection
        }
      },
      { 
        name: 'Name',
        formatter: (cell) => `Name: ${cell}`
      },
      'Email',
  ],
  sort: true,
  data: [
    // Replace these with your actual data
    ["John Doe", "john.doe@example.com"],
    ["Jane Smith", "jane.smith@example.com"],
    ["Alice Johnson", "alice.johnson@example.com"],
    ["Bob Brown", "bob.brown@example.com"],
    ["Charlie Davis", "charlie.davis@example.com"]
  ],
  
}).render(gridContainer2);
 
// grid.on('ready', () => {
//   // find the plugin with the give plugin ID
//   const checkboxPlugin = grid.config.plugin.get('selectRow');
//   // read the selected rows from the plugin's store
//   console.log('selected rows:', checkboxPlugin.props.store.state);
//   console.log("read")
// })

      
</script>

<div class="table-container">
        
  <div class="size-max  relative" bind:this={gridContainer2}>
  
  </div>

  </div> -->