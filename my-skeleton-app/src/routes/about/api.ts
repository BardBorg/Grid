import type { State } from '@vincjo/datatables/remote'


export const reload = async (state: State) => {
    const response = await fetch(
        `http://127.0.0.1:5000/api/data?${getParams(state)}`
    )

    const json=await response.json()
    state.setTotalRows(json.total)
    return json.results
}

const getParams = (state: State) => {
    const { pageNumber, rowsPerPage } = state

    let params = `page=${pageNumber}`

    if (rowsPerPage) {
        params += `&limit=${rowsPerPage}`
    }
    // if (sort) {
    //     params += `&_sort=${sort.orderBy}&_order=${sort.direction}`
    // }
    // if (filters) {
    //     params += filters.map(({ filterBy, value }) => `&${filterBy}=${value}`).join('')
    // }
    // if (search) {
    //     params += `&q=${search}`
    // }
    return params
}
