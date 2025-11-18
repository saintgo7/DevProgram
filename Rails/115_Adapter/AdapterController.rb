class AdapterController < ApplicationController
  before_action :set_adapter, only: [:show, :edit, :update, :destroy]

  # GET /adapter
  def index
    @adapters = Adapter.all
    render json: @adapters
  end

  # GET /adapter/1
  def show
    render json: @adapter
  end

  # POST /adapter
  def create
    @adapter = Adapter.new(adapter_params)

    if @adapter.save
      render json: @adapter, status: :created
    else
      render json: @adapter.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /adapter/1
  def update
    if @adapter.update(adapter_params)
      render json: @adapter
    else
      render json: @adapter.errors, status: :unprocessable_entity
    end
  end

  # DELETE /adapter/1
  def destroy
    @adapter.destroy
    head :no_content
  end

  private

  def set_adapter
    @adapter = Adapter.find(params[:id])
  end

  def adapter_params
    params.require(:adapter).permit(:name)
  end
end
