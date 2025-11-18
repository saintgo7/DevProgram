class RoleController < ApplicationController
  before_action :set_role, only: [:show, :edit, :update, :destroy]

  # GET /role
  def index
    @roles = Role.all
    render json: @roles
  end

  # GET /role/1
  def show
    render json: @role
  end

  # POST /role
  def create
    @role = Role.new(role_params)

    if @role.save
      render json: @role, status: :created
    else
      render json: @role.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /role/1
  def update
    if @role.update(role_params)
      render json: @role
    else
      render json: @role.errors, status: :unprocessable_entity
    end
  end

  # DELETE /role/1
  def destroy
    @role.destroy
    head :no_content
  end

  private

  def set_role
    @role = Role.find(params[:id])
  end

  def role_params
    params.require(:role).permit(:name)
  end
end
