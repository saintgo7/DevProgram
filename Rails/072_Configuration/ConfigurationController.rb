class ConfigurationController < ApplicationController
  before_action :set_configuration, only: [:show, :edit, :update, :destroy]

  # GET /configuration
  def index
    @configurations = Configuration.all
    render json: @configurations
  end

  # GET /configuration/1
  def show
    render json: @configuration
  end

  # POST /configuration
  def create
    @configuration = Configuration.new(configuration_params)

    if @configuration.save
      render json: @configuration, status: :created
    else
      render json: @configuration.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /configuration/1
  def update
    if @configuration.update(configuration_params)
      render json: @configuration
    else
      render json: @configuration.errors, status: :unprocessable_entity
    end
  end

  # DELETE /configuration/1
  def destroy
    @configuration.destroy
    head :no_content
  end

  private

  def set_configuration
    @configuration = Configuration.find(params[:id])
  end

  def configuration_params
    params.require(:configuration).permit(:name)
  end
end
