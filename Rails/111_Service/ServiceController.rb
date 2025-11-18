class ServiceController < ApplicationController
  before_action :set_service, only: [:show, :edit, :update, :destroy]

  # GET /service
  def index
    @services = Service.all
    render json: @services
  end

  # GET /service/1
  def show
    render json: @service
  end

  # POST /service
  def create
    @service = Service.new(service_params)

    if @service.save
      render json: @service, status: :created
    else
      render json: @service.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /service/1
  def update
    if @service.update(service_params)
      render json: @service
    else
      render json: @service.errors, status: :unprocessable_entity
    end
  end

  # DELETE /service/1
  def destroy
    @service.destroy
    head :no_content
  end

  private

  def set_service
    @service = Service.find(params[:id])
  end

  def service_params
    params.require(:service).permit(:name)
  end
end
