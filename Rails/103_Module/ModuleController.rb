class ModuleController < ApplicationController
  before_action :set_module, only: [:show, :edit, :update, :destroy]

  # GET /module
  def index
    @modules = Module.all
    render json: @modules
  end

  # GET /module/1
  def show
    render json: @module
  end

  # POST /module
  def create
    @module = Module.new(module_params)

    if @module.save
      render json: @module, status: :created
    else
      render json: @module.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /module/1
  def update
    if @module.update(module_params)
      render json: @module
    else
      render json: @module.errors, status: :unprocessable_entity
    end
  end

  # DELETE /module/1
  def destroy
    @module.destroy
    head :no_content
  end

  private

  def set_module
    @module = Module.find(params[:id])
  end

  def module_params
    params.require(:module).permit(:name)
  end
end
