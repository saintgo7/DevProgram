class AddressController < ApplicationController
  before_action :set_address, only: [:show, :edit, :update, :destroy]

  # GET /address
  def index
    @addresss = Address.all
    render json: @addresss
  end

  # GET /address/1
  def show
    render json: @address
  end

  # POST /address
  def create
    @address = Address.new(address_params)

    if @address.save
      render json: @address, status: :created
    else
      render json: @address.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /address/1
  def update
    if @address.update(address_params)
      render json: @address
    else
      render json: @address.errors, status: :unprocessable_entity
    end
  end

  # DELETE /address/1
  def destroy
    @address.destroy
    head :no_content
  end

  private

  def set_address
    @address = Address.find(params[:id])
  end

  def address_params
    params.require(:address).permit(:name)
  end
end
