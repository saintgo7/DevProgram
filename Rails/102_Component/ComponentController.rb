class ComponentController < ApplicationController
  before_action :set_component, only: [:show, :edit, :update, :destroy]

  # GET /component
  def index
    @components = Component.all
    render json: @components
  end

  # GET /component/1
  def show
    render json: @component
  end

  # POST /component
  def create
    @component = Component.new(component_params)

    if @component.save
      render json: @component, status: :created
    else
      render json: @component.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /component/1
  def update
    if @component.update(component_params)
      render json: @component
    else
      render json: @component.errors, status: :unprocessable_entity
    end
  end

  # DELETE /component/1
  def destroy
    @component.destroy
    head :no_content
  end

  private

  def set_component
    @component = Component.find(params[:id])
  end

  def component_params
    params.require(:component).permit(:name)
  end
end
