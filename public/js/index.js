let shoppingList = []

class Item {
  constructor(category, name) {
    this.category = category
    this.name = name
  }
  toHTMLItem() {
    return `<li class="list-group-item">${this.name} (${this.category})</li>`
  }
  toString() {
    return this.name
  }
}

function createListItem(item) {
  return item.toHTMLItem()
}

function getCategory(item) {
  return item.category
}

document.querySelector('#add-item').addEventListener('mousedown', (e) => {
  console.log('HERE', e)
  const category = document.querySelector('#item-type-selector').value
  const itemName = document.querySelector('#item-name').value
  const item = new Item(category, itemName)

  shoppingList.push(item)

  updateDOMList()
})

document.querySelector('form').addEventListener('submit', (e) => {
  let list = document.querySelector('[name="list"]')
  let categories = new Set(shoppingList.map(getCategory))
  list.value = ([...categories]).join(',')
})

function updateDOMList() {
  let html = ([...shoppingList]).map(createListItem).join('\n')
  document.querySelector('#shopping-list').innerHTML = html
}