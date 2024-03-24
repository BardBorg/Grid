<script lang="ts">
  // import myData from '$site/data/data'
  import { DataHandler,Datatable, Th, ThFilter, type State } from '@vincjo/datatables/remote'
  import {check} from '@vincjo/datatables'
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import Pagination from './pagination.svelte';
  
//   import Search           from './Search.svelte'

  import { reload } from './api'
    export let data:{ results: any[], total: number}
    
    const handler = new DataHandler(data.results, { rowsPerPage: 10, totalRows: data.total })
    const rows = handler.getRows()
    const selected = handler.getSelected()
   
    handler.onChange((state: State) => reload(state) )


    

  // const handler = new DataHandler([], {rowsPerPage: 10})
  // // const rows = handler.getRows()
  // const selected = handler.getSelected()
  // const isAllSelected = handler.isAllSelected()

  // let handler;
  // const rows = writable([]);

  // onMount(async () => {
    
  //   // try {
  //       const res = await fetch('http://127.0.0.1:5000/api/data');
  //       const data = await res.json();


      

  //       // console.log(data)
  //       const results=data.results
  //     //   handler.setData(data.results);  // Update the DataHandler with the fetched data
  //     // rows.set(handler.getRows());
       
        
        
  //       let dataGrid=[];
  //       for (let i=0; i<18;i++){
  //         dataGrid.push({ 
  //               email: results[i].Email, 
  //               id: results[i].ID, 
  //               name: results[i].Name, 
  //               role: results[i].Role 
  //           });
                                                    
  //       }

  //       rows.set(dataGrid);
  //     });





// const rows=writable(dataGrid);


</script>

<!-- <header>
    <Search {handler} />
</header> -->

<Datatable {handler}>
    <table>
        <thead>
            <tr>
                <Th {handler} orderBy="ID">ID</Th>
                <Th {handler} orderBy="Email">Last Name</Th>
                <Th {handler} orderBy="Name">Email</Th>
                <Th {handler} orderBy="Name">Name</Th>
                <Th {handler} orderBy="Role">Role</Th>
            </tr>
            <!-- <tr><th class="selection" />
                <ThFilter {handler} filterBy="ID"/>
                <ThFilter {handler} filterBy="Email" />
                <ThFilter {handler} filterBy="Name"/>
                <ThFilter {handler} filterBy="Role"/>
            </tr> -->
        </thead>
        <tbody>
            {#each $rows as row}
                <tr class:active={$selected.includes(row.ID)}>
                    <td> <input type="checkbox" 
                        on:click={() => console.log(row.ID)} 
                        checked={$selected.includes(row.ID)}
                    /></td>
                    <!-- <td>{row.ID}</td> -->
                    <td>{row.ID}</td>
                    <td>{row.Email}</td>
                    <td>{row.Name}</td>
                    <td>{row.Role}</td>

                </tr>
            {/each}
        </tbody>
    </table>
    <!-- <main>
        
        <Pagination {handler}/>
      </main> -->
</Datatable>




<style>
    thead {
        background: #fff;
       color: black;
    }
    thead th.selection {
        width: 40px;
        padding-left: 8px;
        border-bottom: 1px solid #e0e0e0;
    }
    tbody td {
        border: 1px solid #f5f5f5;
        padding: 2px 16px;
    }
    tbody tr {
        transition: all, 0.2s;
        
    }
    tbody tr:hover {
        background: #fafafa;
        color:black;
        cursor: pointer;
    }
    b {
        color: var(--r-primary);
        font-weight: normal;
        line-height: 16px;
        white-space:break-spaces;
    }
    span {
        padding-left: 8px;
    }
</style>