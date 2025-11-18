class FactoryController < ApplicationController
  before_action :set_factory, only: [:show, :edit, :update, :destroy]

  # GET /factory
  def index
    @factorys = Factory.all
    render json: @factorys
  end

  # GET /factory/1
  def show
    render json: @factory
  end

  # POST /factory
  def create
    @factory = Factory.new(factory_params)

    if @factory.save
      render json: @factory, status: :created
    else
      render json: @factory.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /factory/1
  def update
    if @factory.update(factory_params)
      render json: @factory
    else
      render json: @factory.errors, status: :unprocessable_entity
    end
  end

  # DELETE /factory/1
  def destroy
    @factory.destroy
    head :no_content
  end

  private

  def set_factory
    @factory = Factory.find(params[:id])
  end

  def factory_params
    params.require(:factory).permit(:name)
  end
end
