# Current Location Feature

The homepage displays your current location in a prominent banner, powered by a data file.

## How to Update Your Location

Edit the `data/location.yaml` file:

```yaml
current:
  place: "Baja California Sur, Mexico"
  region: "Baja California Sur"
  country: "Mexico"
  description: "Exploring the beaches and desert landscapes of Baja"
  coordinates:
    lat: 24.1426
    lon: -110.3128
  updated: "2025-10-04"
```

### Fields:

- **place** - Where you are (city, region, country) - **Required**
- **region** - State/province (optional, for future filtering)
- **country** - Country (optional, for future filtering)
- **description** - Brief note about what you're doing (optional)
- **coordinates** - Lat/lon for future map integration (optional)
- **updated** - Date you last updated this - **Required**

### To Update:

1. Edit `data/location.yaml`
2. Change the values under `current:`
3. Commit and push:

```bash
git add data/location.yaml
git commit -m "Update current location to [Place]"
git push
```

Netlify will automatically rebuild and deploy in ~2 minutes.

## Examples

### Simple location:
```yaml
current:
  place: "Todos Santos, Baja California Sur"
  updated: "2025-10-10"
```

### With full details:
```yaml
current:
  place: "La Paz, Baja California Sur"
  region: "Baja California Sur"
  country: "Mexico"
  description: "Stocking up on supplies and exploring the malecon"
  coordinates:
    lat: 24.1426
    lon: -110.3128
  updated: "2025-10-15"
```

### Back home:
```yaml
current:
  place: "Pagosa Springs, Colorado"
  region: "Colorado"
  country: "USA"
  description: "Home at basecamp for the winter"
  coordinates:
    lat: 37.2694
    lon: -107.0097
  updated: "2025-11-01"
```

## Location History (Optional)

You can track your travel history in the same file:

```yaml
current:
  place: "Current Location"
  updated: "2025-10-04"

history:
  - place: "Pagosa Springs, Colorado"
    arrived: "2025-09-15"
    departed: "2025-09-28"
    notes: "Basecamp - preparing for Baja trip"
  
  - place: "Durango, Colorado"
    arrived: "2025-09-10"
    departed: "2025-09-14"
    notes: "Last minute supplies"
```

This history isn't displayed yet, but it's ready for future features like:
- Travel timeline
- Map of places visited
- Stats (days traveled, locations visited)

## To Hide the Location Banner

Delete or comment out the `current:` section in `data/location.yaml`:

```yaml
# current:
#   place: "Somewhere"
#   updated: "2025-10-04"
```

## Why Use Data Files?

**Benefits:**
- ✅ Separates content from configuration
- ✅ Easier to update (just edit one YAML file)
- ✅ Can be automated (scripts, APIs, etc.)
- ✅ Supports structured data (coordinates, dates, etc.)
- ✅ Can track history
- ✅ Future-proof for features like maps, timelines, stats

**Similar to your markgroves.us webmentions setup!**

## Future Enhancements

With this data structure, we can easily add:
- Interactive map showing current location
- Timeline of all locations visited
- Stats dashboard (days traveled, countries visited)
- Filter posts by location
- Automatic weather display
- Distance traveled calculations
- Photo galleries by location

## Data File Format

Hugo supports multiple formats:
- **YAML** (`.yaml` or `.yml`) - Human-readable, recommended
- **JSON** (`.json`) - Machine-readable
- **TOML** (`.toml`) - Alternative to YAML

We're using YAML because it's easiest to read and edit.

## Accessing Data in Templates

The location data is available in templates as:

```go
{{ .Site.Data.location.current.place }}
{{ .Site.Data.location.current.description }}
{{ .Site.Data.location.current.coordinates.lat }}
{{ .Site.Data.location.history }}
```

This makes it easy to use the data anywhere on your site!
