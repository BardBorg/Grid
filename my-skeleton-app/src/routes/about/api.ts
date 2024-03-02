import type { State } from '@vincjo/datatables/remote'


export const reload = async (state: State) => {
    const response = await fetch(
        `http://127.0.0.1:5000/api/data?${getParams(state)}`
    )

    const json=await response.json()
    state.setTotalRows(json.total)
    return json.results
}

const getParams = ({ pageNumber, rowsPerPage }: State) => {

    let params = `_page=${pageNumber}`

    if (rowsPerPage) {
        params += `&_limit=${rowsPerPage}`
    }
  

    return params
}
