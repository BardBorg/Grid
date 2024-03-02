<script lang="ts">
  // import myData from '$site/data/data'
  import { DataHandler, Datatable, Th, ThFilter, type State } from '@vincjo/datatables/remote'
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  import { reload } from './api'
    export let data:{ results: any[], total: number}

    const handler = new DataHandler(data.results, { rowsPerPage: 20, totalRows: data.total })
    const rows = handler.getRows()

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



<Datatable {handler}>
    <table>
        <thead>
            <tr>
                <Th {handler} orderBy="ID">First Name</Th>
                <Th {handler} orderBy="Email">Last Name</Th>
                <Th {handler} orderBy="Name">Email</Th>
                <Th {handler} orderBy="Role">Role</Th>
            </tr>
            <tr>
                <ThFilter {handler} filterBy="ID"/>
                <ThFilter {handler} filterBy="Email" />
                <ThFilter {handler} filterBy="Name"/>
                <ThFilter {handler} filterBy="Role"/>
            </tr>
        </thead>
        <tbody>
            {#each $rows as row}
                <tr>
                    <td>{row.ID}</td>
                    <td>{row.Email}</td>
                    <td>{row.Name}</td>
                    <td>{row.Role}</td>

                </tr>
            {/each}
        </tbody>
    </table>
</Datatable>

<style>
    thead {
        background: #fff;
    }
    tbody td {
        border: 1px solid #f5f5f5;
        padding: 4px 20px;
    }
    tbody tr {
        transition: all, 0.2s;
    }
    tbody tr:hover {
        background: #f5f5f5;
    }
</style>
