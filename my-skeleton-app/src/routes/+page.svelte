
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
        let dataGrid=[];
        let value;
        let length=10;
        let count=0;
      

        $: kolejne=count
        $: dlugosc=length
        // let grid;
   function left(){




   }
   function right(){
    
    
    count+=10;
    length+=10;
    

   }
   function hide(){

   }

  let grid;

   onMount(async () => {
       
        // try {
            const res = await fetch('http://127.0.0.1:5000/api/data');
            const data = await res.json();
            // console.log(data)
            const results=data.results
            // message = data.message;
            // const data2=JSON.stringify(data);
            // const json=JSON.parse(data);
            // name=data[0].Name;
            // ids=data[0].ID;
            // email=data[0].Email;
            // role=data[0].Role;
            // ids=data.ID;
            // email=data.Email;
            // role=data.Role;
           
            // userData[0] = { id: ids, name: name, email: email, role: role }; // Update the first element of the array
            
            
            for (let i=0; i<10;i++){
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


//         grid.config.store.subscribe(function (state) {
//   console.log('checkbox updated', state.rowSelection);
// })

// grid.config.store.subscribe(function (state) {
//   console.log('checkbox updated', state.rowSelection);
// })





    });

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
  // console.log(value)
  const cellValue = dataGrid[3];
  // // const cellValue=row.cells[0].data;
  console.log(cellValue);
  

  }
        let gridContainer;
      
        // onMount(() => {
 
        // });

      //  console.log(value)

//        grid.on('ready', () => {
//   // find the plugin with the give plugin ID
//   const checkboxPlugin = grid.config.plugin.get('selectRow');
//   // read the selected rows from the plugin's store
//   console.log('selected rows:', checkboxPlugin.props.store.state);
// })


function readSelectedRows() {
  // const checkboxPlugin = grid.config.plugin.get('Checkbox')
  //         // read the selected rows from the plugin's store
  //         checkboxPlugin.props.store.on('updated', function (state) {
  //           console.log('checkbox updated', state);
  //         });

 //Ensure grid instance is available
//  const selectedData = grid.config.plugin.get('Checkbox').props.store.state.selectedRows;
//     console.log('Selected rows:', selectedData);

  }

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
 <!-- <button on:click={left}>Strona do tyłu</button> -->
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