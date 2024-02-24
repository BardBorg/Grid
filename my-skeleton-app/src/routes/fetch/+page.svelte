<!-- <script>
	import Grid from "gridjs-svelte"

	const columns = [
		{
			name: 'Title',
			sort: false
		},
		{
			name: 'Date',
			formatter: cell => {
				return new Date(cell).toLocaleString('en-US', {
					month: 'short',
					year: 'numeric'
				})
			}
		}
	]
</script>

<Grid
	{columns}
	sort
	search
	pagination={{ enabled: true, limit: 3 }}
	server={{
		url: 'https://swapi.dev/api/films/',
		then: data => data.results.map(movie => {
			return [movie.title, movie.release_date]
		})
	}}
/>

<style global>
  @import "https://cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css";
</style> -->