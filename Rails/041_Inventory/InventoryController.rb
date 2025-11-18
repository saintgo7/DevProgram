class InventoryController < ApplicationController
  before_action :set_inventory, only: [:show, :edit, :update, :destroy]

  # GET /inventory
  def index
    @inventorys = Inventory.all
    render json: @inventorys
  end

  # GET /inventory/1
  def show
    render json: @inventory
  end

  # POST /inventory
  def create
    @inventory = Inventory.new(inventory_params)

    if @inventory.save
      render json: @inventory, status: :created
    else
      render json: @inventory.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /inventory/1
  def update
    if @inventory.update(inventory_params)
      render json: @inventory
    else
      render json: @inventory.errors, status: :unprocessable_entity
    end
  end

  # DELETE /inventory/1
  def destroy
    @inventory.destroy
    head :no_content
  end

  private

  def set_inventory
    @inventory = Inventory.find(params[:id])
  end

  def inventory_params
    params.require(:inventory).permit(:name)
  end
end
