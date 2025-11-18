class LDAPController < ApplicationController
  before_action :set_ldap, only: [:show, :edit, :update, :destroy]

  # GET /ldap
  def index
    @ldaps = LDAP.all
    render json: @ldaps
  end

  # GET /ldap/1
  def show
    render json: @ldap
  end

  # POST /ldap
  def create
    @ldap = LDAP.new(ldap_params)

    if @ldap.save
      render json: @ldap, status: :created
    else
      render json: @ldap.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /ldap/1
  def update
    if @ldap.update(ldap_params)
      render json: @ldap
    else
      render json: @ldap.errors, status: :unprocessable_entity
    end
  end

  # DELETE /ldap/1
  def destroy
    @ldap.destroy
    head :no_content
  end

  private

  def set_ldap
    @ldap = LDAP.find(params[:id])
  end

  def ldap_params
    params.require(:ldap).permit(:name)
  end
end
