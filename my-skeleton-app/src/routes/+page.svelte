
    <!-- <link rel='stylesheet' href='/styles/style.css'> -->

    <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
   

    <script>
        import { onMount } from 'svelte';
        import { Grid, html} from "gridjs";
        import "gridjs/dist/theme/mermaid.css";
        import { RowSelection } from "gridjs/plugins/selection";
        import { Search, Button } from 'flowbite-svelte';
        import { PluginPosition } from "gridjs";
        
        let name;
        let email;
        let role;
        
        let value;
        let length=10;
        let count=0;
        let test="test";

        $: kolejne=count
        $: dlugosc=length
        // let grid;
   
   
let dataGrid=[];
  let grid;

   onMount(async () => {
    
        // try {
            const res = await fetch('http://127.0.0.1:5000/api/data');
            const data = await res.json();
            // console.log(data)
            const results=data.results
           
           
            
            
        
            for (let i=0; i<18;i++){
              dataGrid.push({ 
                    email: results[i].Email, 
                    id: results[i].ID, 
                    name: results[i].Name, 
                    role: results[i].Role 
                });
                                                        
            }
          
        
         grid = new Grid({
        columns: [
          {
            id: 'selectRow',
            name: 'Select',
            plugin: {
              component: RowSelection, // Make sure to import RowSelection
              props: {
                id: (row) => row.cell(3).data, // Assuming ID is the unique identifier, rozwiazanie do grimora
              },
            },
          },
          'Name',
          { id: 'email', name: 'Email' },
          { id: 'id', name: 'ID' },
          'Role'
        ],
        data: dataGrid,
        sort: true,
        search: true,
        pagination: {
          enabled: true,
          limit: 5,
          summary: true
        },
            style: {
    table: {
      border: '3px solid #ccc'
    },
    th: {
      'background-color': 'rgba(30, 115, 0, 100.1)',
      color: '#000',
      'border-bottom': '3px solid #ccc',
      'text-align': 'center',
      
    },
    td: {
      'text-align': 'center',
      
    }
  }
  
            // any other grid options...
          }).render(gridContainer);
            
        // } catch (err) {
        //     name = 'Failed to fetch data from the server';
        // }


//         



   
        
    });

    $: console.log(dataGrid);


    function refresh(){
      
      dataGrid = dataGrid.filter((item, index) => index !== 2);
      
    }
 

    function read(){
    // grid.on('ready', () => {
  // find the plugin with the give plugin ID
  const checkboxPlugin = grid.config.plugin.get('selectRow');
  // // read the selected rows from the plugin's store
  console.log('selected rows:', checkboxPlugin.props.store.state);
  console.log("ready")
// })
}

   
 function search(){
 
  // const cellValue = dataGrid[3];
  // // // const cellValue=row.cells[0].data;
  
 
  

  }
        let gridContainer;
      




 

  

//   grid.on('headerClick', (column) => {    //To powoduje niewyswietlanie gridu. Sluzy do interakcji z kolumnami.
//     if (column.id === 'myColumnId') {
//         // Apply custom sorting or other actions
//     }
// });
      </script>
      
      <div class="table-container">
        
      <div class="size-max  relative" bind:this={gridContainer}>
      
      </div>
      
          <!-- <form class="w-32  m-auto w-1/2 " id="Search" on:keyup={search} >
          <Search bind:value class="text-black absolute"/>
          <p></p>  
        </form> -->
      </div>
          

      
      
 <!-- <h1>{name}</h1> -->
 <button class="bg-white-950" on:click={refresh}>Filter</button>
<button class="bg-green-950" on:click={search} >Get cell value</button>
<button class="bg-red-950" id="read-selected-rows-btn" on:click={read}>Pokaż wybrany wiersz</button>

      
















<!-- YOU CAN DELETE EVERYTHING IN THIS PAGE -->
<!-- <script>
import Grid from "gridjs-svelte"

const data = [
  { name: "John", email: "john@example.com" },
  { name: "Mark", email: "mark@gmail.com" },
]
</script>

<Grid data={data} />

<style global>
@import "https://cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css";
</style> -->

<!-- <script>
    import { onMount } from 'svelte';

    let message = 'Loading...';

    onMount(async () => {
        try {
            const res = await fetch('http://localhost:5000/api/data');
            const data = await res.json();
            message = data.message;
        } catch (err) {
            message = 'Failed to fetch data from the server';
        }
    });

	</script> -->

<!-- <h1>{message}</h1> -->