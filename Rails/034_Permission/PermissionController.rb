class PermissionController < ApplicationController
  before_action :set_permission, only: [:show, :edit, :update, :destroy]

  # GET /permission
  def index
    @permissions = Permission.all
    render json: @permissions
  end

  # GET /permission/1
  def show
    render json: @permission
  end

  # POST /permission
  def create
    @permission = Permission.new(permission_params)

    if @permission.save
      render json: @permission, status: :created
    else
      render json: @permission.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /permission/1
  def update
    if @permission.update(permission_params)
      render json: @permission
    else
      render json: @permission.errors, status: :unprocessable_entity
    end
  end

  # DELETE /permission/1
  def destroy
    @permission.destroy
    head :no_content
  end

  private

  def set_permission
    @permission = Permission.find(params[:id])
  end

  def permission_params
    params.require(:permission).permit(:name)
  end
end
